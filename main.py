from pathlib import Path
from src.utils import init_table, search, heuristic_one, heuristic_two, count_inversions
import time
from scipy.optimize import brentq
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tqdm import tqdm 
from argparse import ArgumentParser


def effective_branching_factor(N: int, d: int):
    if d == 0:
        return 0
    if N <= d:
        return 1.0
    func = lambda b: sum(b**i for i in range(d + 1)) - (N + 1)
    return brentq(func, 1.0, max(N + 1, 2.0), xtol=1e-4)


def main(verbose: bool = False):
    print("Running experiments...")
    num_tests = 100
    data = []
    heuristics = {"one": heuristic_one, "two": heuristic_two}
    depths = [2, 4, 8, 12, 16, 18, 20, 22, 24, 26]
    root_path = Path(__file__).parent
    assets_path = root_path / "assets"
    assets_path.mkdir(exist_ok=True)

    for dep in depths:
        for i in range(num_tests):
            table, desired_state = init_table(9, dep)
            assert count_inversions(table) % 2 == 0, "init_table gerou estado insolúvel"
            if verbose:
                print(f"Test {i+1}/{num_tests} - Depth {dep}")
                print(table)
                print(desired_state)

            pbar = tqdm(total=len(heuristics), desc=f"Depth {dep} - Test {i+1}/{num_tests}", leave=False)
            for key in heuristics.keys():
                b = [1]
                start = time.perf_counter()

                solved, path = search(
                    table, desired_state, b, heuristic=heuristics[key]
                )
                d = len(path) - 1
                b_star = effective_branching_factor(b[0], d)

                if verbose:
                    print(f"Número de movimentos: {len(path) - 1}")
                end = time.perf_counter()

                cell = {
                    "tempo_exec": end - start,
                    "b*": b_star,
                    "sol": str(path),
                    "heuristic": key,
                    "depth": dep,
                }

                data.append(cell)
                pbar.update(1)
                if verbose:
                    print(f"Tempo de execução: {end - start:.2f}")
                    print(f"b* {b_star}z")

            pbar.close()

    df = pd.DataFrame(data)
    df.to_csv(assets_path / "experiments_result.csv", index=False)

    # now, lets plot data
    sns.set_style("whitegrid")
    # plot b*, depth, and heuristic on the same graph
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="depth", y="b*", hue="heuristic", marker="o")
    plt.title("Effective Branching Factor (b*) vs Depth for Different Heuristics")
    plt.xlabel("Depth")
    plt.ylabel("Effective Branching Factor (b*)")
    plt.legend(title="Heuristic")
    if verbose:
        plt.show()
    fig.savefig(assets_path / "b_star_vs_depth.png")

    # plot execution time, depth, and heuristic on the same graph
    fig2 = plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="depth", y="tempo_exec", hue="heuristic", marker="o")
    plt.title("Execution Time vs Depth for Different Heuristics")
    plt.xlabel("Depth")
    plt.ylabel("Execution Time (seconds)")
    plt.legend(title="Heuristic")
    if verbose:
        plt.show()
    # save figures 
    fig2.savefig(assets_path / "execution_time_vs_depth.png")


if __name__ == "__main__":
    parser = ArgumentParser(description="Run A* algorithm experiments")
    parser.add_argument(
            "--verbose", "-v", action="store_true", help="Enable verbose output during experiments"
    )
    args = parser.parse_args()
    main(args.verbose)
