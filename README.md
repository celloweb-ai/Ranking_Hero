## 🏆 Calculadora de Partidas Rankeadas (Ranking Hero)

A Calculadora de Partidas Rankeadas é um algoritmo simples e versátil projetado para demonstrar o uso de estruturas condicionais, funções e classes na programação, classificando um jogador em um nível de rank baseado no número total de vitórias.

Este projeto inclui implementações em **JavaScript** e **Python**, oferecendo diferentes abordagens, desde a funcional básica até uma versão orientada a objetos com um relatório completo.

-----

### 🌟 Lógica do Sistema

O ranqueamento do Herói é determinado exclusivamente pelo **número total de vitórias** (`vitorias`) e a mensagem de exibição informa o **saldo de vitórias** (`saldo`), calculado por:

$$\text{saldo} = \text{vitórias} - \text{derrotas}$$

A classificação dos níveis segue os seguintes critérios condicionais:

| Nível (Rank) | Critério de Vitórias (`vitorias`) |
| :----------: | :-------------------------------: |
| **Ferro** | Menos de 10 vitórias              |
| **Bronze** | Entre 11 e 20 vitórias            |
| **Prata** | Entre 21 e 50 vitórias            |
| **Ouro** | Entre 51 e 80 vitórias            |
| **Diamante** | Entre 81 e 90 vitórias            |
| **Lendário** | Entre 91 e 100 vitórias           |
| **Imortal** | 101 vitórias ou mais              |

-----

### 💻 Implementação em JavaScript

Esta é a versão **básica e recomendada** do algoritmo em JavaScript, que utiliza a estrutura `if-else if` para verificar os intervalos de vitórias de forma concisa.

```javascript
/**
 * Função para calcular o saldo de vitórias e determinar o nível do Herói.
 * @param {number} vitorias - O número total de vitórias do Herói.
 * @param {number} derrotas - O número total de derrotas do Herói.
 * @returns {string} Mensagem formatada com o saldo e o nível.
 */
function calculadoraRankeadas(vitorias, derrotas) {
    // 1. Calcula o saldo de rankeadas
    const saldoVitorias = vitorias - derrotas;
    let nivel = "";

    // 2. Estrutura condicional para determinar o nível
    if (vitorias < 10) {
        nivel = "Ferro";
    } else if (vitorias <= 20) { // Assume 10-20 (com base na lógica do projeto original)
        nivel = "Bronze";
    } else if (vitorias <= 50) { // Assume 21-50
        nivel = "Prata";
    } else if (vitorias <= 80) { // Assume 51-80
        nivel = "Ouro";
    } else if (vitorias <= 90) { // Assume 81-90
        nivel = "Diamante";
    } else if (vitorias <= 100) { // Assume 91-100
        nivel = "Lendário";
    } else { // 101 ou mais
        nivel = "Imortal";
    }

    // 3. Retorna a mensagem formatada
    return `O Herói tem saldo de ${saldoVitorias} e está no nível de ${nivel}`;
}

// Exemplos de uso
console.log(calculadoraRankeadas(5, 2));    // Ferro
console.log(calculadoraRankeadas(15, 5));   // Bronze
console.log(calculadoraRankeadas(110, 15)); // Imortal
```

#### ✨ Versão Otimizada com Array (JavaScript)

Uma abordagem mais moderna (ES6+) que utiliza um `Array` de configuração para definir os limites e o método `Array.prototype.find()` para determinar o nível.

```javascript
const calculadoraRankOtimizada = (vitorias, derrotas) => {
    const saldoVitorias = vitorias - derrotas;

    // Array de configuração dos níveis: [limite (exclusivo), nome]
    const niveis = [
        [10, "Ferro"],
        [20, "Bronze"],
        [50, "Prata"],
        [80, "Ouro"],
        [90, "Diamante"],
        [100, "Lendário"],
        [Infinity, "Imortal"] // Para 101+ vitórias
    ];

    // Busca o primeiro nível onde o número de vitórias é MENOR que o limite
    const nivel = niveis.find(([limite]) => vitorias < limite)[1];

    return `O Herói tem saldo de ${saldoVitorias} e está no nível de ${nivel}`;
};

// Exemplo
console.log(calculadoraRankOtimizada(65, 15)); // Ouro
```

-----

### 🐍 Implementação em Python

#### 📜 Versão Funcional Básica (Python)

Uma implementação direta da lógica do sistema usando uma função e estruturas condicionais.

```python
def calculadora_rankeadas(vitorias: int, derrotas: int) -> str:
    """
    Calcula o saldo de ranqueadas e determina o nível do jogador.

    Args:
        vitorias: Número de vitórias.
        derrotas: Número de derrotas.

    Returns:
        Mensagem com saldo e nível do jogador.
    """
    # Calcula o saldo
    saldo_vitorias = vitorias - derrotas

    # Determina o nível usando estruturas condicionais
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return f"O Herói tem saldo de {saldo_vitorias} e está no nível de {nivel}"

# Exemplos de uso
print(calculadora_rankeadas(8, 3))      # Ferro
print(calculadora_rankeadas(72, 18))    # Ouro
print(calculadora_rankeadas(120, 30))   # Imortal
```

#### 🛡️ Versão Avançada com Classe (Python - Orientada a Objetos)

Esta versão utiliza uma **classe** (`CalculadoraRank`) para encapsular a lógica e fornecer funcionalidades adicionais, como o cálculo da taxa de vitória e um relatório detalhado.

```python
class CalculadoraRank:
    """Classe para gerenciar o sistema de ranqueamento, incluindo lógica de nível e relatórios."""

    def __init__(self):
        # Configuração dos ranks: (limite exclusivo de vitórias, nome do rank)
        # O limite 10 atende "menos de 10 vitórias"
        self.ranks = [
            (10, "Ferro"),
            (20, "Bronze"),
            (50, "Prata"),
            (80, "Ouro"),
            (90, "Diamante"),
            (100, "Lendário"),
            (float('inf'), "Imortal") # Último caso, 101+
        ]

    def calcular_saldo(self, vitorias: int, derrotas: int) -> int:
        """Calcula o saldo de vitórias."""
        return vitorias - derrotas

    def determinar_nivel(self, vitorias: int) -> str:
        """Determina o nível baseado nas vitórias."""
        for limite, nivel in self.ranks:
            if vitorias < limite:
                return nivel
        return "Erro de Nível" # Não deve ocorrer

    def calcular_porcentagem_vitorias(self, vitorias: int, derrotas: int) -> float:
        """Calcula a porcentagem de vitórias."""
        total_jogos = vitorias + derrotas
        if total_jogos == 0:
            return 0.0
        return round((vitorias / total_jogos) * 100, 2)

    def gerar_relatorio(self, vitorias: int, derrotas: int) -> dict:
        """Gera um relatório completo do jogador."""
        saldo = self.calcular_saldo(vitorias, derrotas)
        nivel = self.determinar_nivel(vitorias)
        porcentagem = self.calcular_porcentagem_vitorias(vitorias, derrotas)

        return {
            'vitorias': vitorias,
            'derrotas': derrotas,
            'saldo': saldo,
            'nivel': nivel,
            'porcentagem_vitorias': porcentagem,
            'total_partidas': vitorias + derrotas
        }

    def exibir_resultado(self, vitorias: int, derrotas: int) -> str:
        """Exibe resultado formatado em um relatório e retorna a mensagem principal."""
        relatorio = self.gerar_relatorio(vitorias, derrotas)

        print(f"\n{'='*50}")
        print(f"RELATÓRIO DE RANQUEAMENTO")
        print(f"{'='*50}")
        print(f"Vitórias: {relatorio['vitorias']}")
        print(f"Derrotas: {relatorio['derrotas']}")
        print(f"Total de Partidas: {relatorio['total_partidas']}")
        print(f"Saldo: {relatorio['saldo']}")
        print(f"Taxa de Vitória: {relatorio['porcentagem_vitorias']}%")
        print(f"Nível: {relatorio['nivel']}")
        print(f"{'='*50}\n")

        return f"O Herói tem saldo de {relatorio['saldo']} e está no nível de {relatorio['nivel']}"

# Exemplo de uso da classe
calculadora = CalculadoraRank()
print(calculadora.exibir_resultado(95, 20))
```

-----

### 💡 Próximos Passos e Melhorias

O projeto pode ser expandido com funcionalidades adicionais para torná-lo mais robusto e completo:

  * **Validação de Entrada:** Adicionar verificações rigorosas para garantir que os inputs (`vitorias`, `derrotas`) sejam números inteiros, não-negativos e válidos.
  * **Interface Gráfica (GUI):** Criar uma interface web básica com HTML/CSS/JavaScript ou utilizar bibliotecas Python (como Tkinter, Streamlit ou Flask) para uma interação visual.
  * **Banco de Dados:** Implementar o armazenamento de dados do jogador e histórico de partidas para manter um registro persistente do progresso.
  * **Múltiplas Lógicas:** Adicionar diferentes critérios de ranqueamento (ex: ranquear por Saldo em vez de Vitórias Totais).

-----

### 🚀 Como Implementar

1.  **Escolha a Linguagem:** Decida se irá usar a implementação em **JavaScript** (ideal para front-end web) ou **Python** (ideal para back-end ou scripts de console).
2.  **Crie o Arquivo:**
      * Para JavaScript: Crie um arquivo `calculadora_rank.js`.
      * Para Python: Crie um arquivo `calculadora_rank.py`.
3.  **Copie e Cole:** Cole o código da versão de sua preferência no arquivo criado.
4.  **Execute:**
      * **JavaScript (Node.js):** `node calculadora_rank.js`
      * **Python:** `python calculadora_rank.py`

**Dica:** Para projetos front-end em JavaScript, você pode usar a [Versão Interativa para HTML] e criar um arquivo `index.html` para uma demonstração instantânea no navegador.
