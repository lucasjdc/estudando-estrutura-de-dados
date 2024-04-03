using System;
using System.Collections.Generic;

class Program {
	static void Main() {

		// Criando uma fila de inteiros
		Queue<int> minhaFila = new Queue<int>();

		// Adicionando elementos à fila
		minhaFila.Enqueue(10);
		minhaFila.Enqueue(20);
		minhaFila.Enqueue(30);

		// Exibindo os elementos da fila
		Console.WriteLine("Elementos da fila: ");
		foreach (int item in minhaFila) {
			Console.WriteLine(item);
		}

		// Removendo o primeiro elemento da fila
		int primeiroElemento = minhaFila.Dequeue();
		Console.WriteLine("Elemento removido: {0}", primeiroElemento);

		// Exibindo os elementos restantes na fila após a remoção
		Console.WriteLine("Elementos restantes na fila após a remoção:");
		foreach (int item in minhaFila)
		{
			Console.WriteLine(item);
		}

		// Verificando se a fila contém um elemento específico
		int elementoBuscado = 20;
		string elementoEncontrado = minhaFila.Contains(elementoBuscado) ? "Sim" : "Não";		
		Console.WriteLine("A fila contém o elemento {0}?", elementoBuscado);
		Console.WriteLine("R: {0}", elementoEncontrado);

		// Obtendo o primeiro elementro da fila sem removê-lo
		int primeiroElementoSemRemover = minhaFila.Peek();
		Console.WriteLine("O primeiro elemento da fila (sem removê-lo) é: {0}", primeiroElementoSemRemover);

		// Limpando a fila
		minhaFila.Clear();
		Console.WriteLine("A fila foi limpa.");
	}
}