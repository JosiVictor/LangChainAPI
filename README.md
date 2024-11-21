# LangChain Translation API

Este projeto contém uma API simples usando FastAPI e LangChain para realizar traduções entre diferentes idiomas e simular um chatbot com Fake LLM.

1. **Chatbot Simples com Fake LLM**  
   - Um chatbot que simula respostas pré-definidas utilizando o `FakeListLLM` da LangChain.
   
2. **Tradutor com OpenAI**  
   - Traduza textos de inglês para francês usando a API da OpenAI integrada com LangChain.
   
3. **Tradutor com HuggingFace**  
   - Traduza textos de inglês para alemão utilizando o modelo `Helsinki-NLP/opus-mt-en-de` da HuggingFace via LangChain.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construir APIs rápidas.
- **LangChain**: Framework para integrar modelos de linguagem e APIs.
- **OpenAI API**: Para tradução de textos entre inglês e francês.
- **HuggingFace API**: Para tradução de textos entre inglês e alemão.
- **Pydantic**: Para validação de dados de entrada.

## Como Executar

```bash
1. Clone o repositório:
   git clone <URL_DO_REPOSITORIO>

2. Instale as dependências:
   pip install -r requirements.txt

3. Variáveis de ambiente para as APIs:
   OPENAI_API_KEY: Sua chave de API do OpenAI.
   HUGGINGFACEHUB_API_TOKEN: Seu token da HuggingFace.

4. Iniciar a aplicação:
   uvicorn main:app --reload

5. Acessar a API:
   - Chatbot: POST /chatbot/
   - Tradutor (OpenAI): POST /translate/
   - Tradutor (HuggingFace): POST /translate_to_german/
