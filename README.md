# Conversor de Moeda (Reais para Dólares)

## 📌 Descrição
Este é um aplicativo web simples para conversão de moeda, permitindo converter um valor em reais (BRL) para dólares americanos (USD) com base na taxa de câmbio atual. A aplicação utiliza **Flask** para o backend e **Bootstrap/Tailwind CSS** para estilização.

## 🚀 Funcionalidades
- Interface simples e responsiva
- Conversão de BRL para USD em tempo real
- Consumo da API [ExchangeRate-API](https://www.exchangerate-api.com/) para obter a taxa de câmbio

## 🛠 Tecnologias Utilizadas
- **Python** (Flask)
- **HTML5, CSS3 (Bootstrap/Tailwind CSS)**
- **JavaScript** (caso precise de melhorias futuras)
- **ExchangeRate-API**

## 📂 Estrutura do Projeto
```
📁 projeto-conversor
│-- 📁 static
│   └── style.css  # Arquivo de estilos
│-- 📁 templates
│   └── index.html  # Interface principal
│-- app.py  # Lógica principal da aplicação Flask
│-- README.md  # Documentação
```

## ▶ Como Executar o Projeto
1. **Clone este repositório**
   ```sh
   git clone https://github.com/seuusuario/projeto-conversor.git
   cd projeto-conversor
   ```

2. **Crie um ambiente virtual e ative-o**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```sh
   pip install flask requests
   ```

4. **Execute o servidor Flask**
   ```sh
   python app.py
   ```

5. **Abra no navegador**
   ```
   http://127.0.0.1:5000/
   ```

## 📌 API Utilizada
A aplicação utiliza a **ExchangeRate-API** para obter a taxa de câmbio atual. Caso queira utilizar sua própria chave de API, edite a variável `url` no arquivo `app.py`:
```python
url = 'https://v6.exchangerate-api.com/v6/SUA_CHAVE_AQUI/latest/USD'
```

## 🎯 Melhorias Futuras
- Adicionar suporte a outras moedas
- Melhorar a interface com JavaScript dinâmico
- Implementar tratamento de erros mais robusto

## 📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para utilizá-lo e modificá-lo!

---

Feito por [Pedro Vitor RIbeiro Silva](https://github.com/Pedro-Vitor-Ribeiro-Silva) 🚀

