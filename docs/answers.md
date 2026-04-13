Como auxilio nas respostas, veja os gráficos na pasta [assets](../assets/):
- [b* vs profundidade](../assets/b_star_vs_depth.png)
- [tempo de execução vs tempo](../assets/execution_time_vs_depth.png)

1) A heurística 2 ($h_2$) apresentou menor fator de ramificação efetivo b* (curva laranja abaixo da azul) e menor tempo de execução em todas as profundidades, sendo claramente superior em eficiência.

2) Sim. $h_2$ domina $h_1$, e os gráficos confirmam isso sem contradição: como $h_2$ estima valores mais próximos do custo real, o A* expande menos nós, resultando em b* menor e tempo de execução significativamente menor (especialmente em profundidades maiores, onde h₁ chega a ~0.25s contra ~0.06s de $h_2$).

3) Ambas são admissíveis pois nunca superestimam o custo real — os b* próximos de 1.3–1.5 confirmam que o algoritmo está encontrando soluções ótimas. Se uma heurística superestimasse, o A* poderia descartar o caminho ótimo, retornando soluções subótimas.

4) A limitação principal é o crescimento exponencial de memória: pelo gráfico de tempo, mesmo em profundidade ~27 o tempo já explode para $h_1$; para o quebra-cabeça de 15 peças (profundidades na casa de 50+), o A* precisaria armazenar bilhões de nós, tornando-o inviável sem variantes como IDA* (como visto em aula).
