# 📷 HEIConverter – Conversor de Imagens HEIC para JPEG

**HEIConverter** é uma aplicação Python com interface gráfica que converte imagens no formato HEIC para JPEG. Foi desenvolvido utilizando `Pillow` e `pillow-heif`, com suporte opcional à containerização via Docker.

## 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- Pillow
- pillow-heif
- Docker (opcional)

## 📁 Estrutura do Projeto

- `app.py`: Script principal da aplicação.
- `requirements.txt`: Dependências do projeto.
- `Dockerfile`: Configuração para containerização da aplicação.


## ⚙️ Como Executar

### 🖥️ Modo Local

```bash
git clone https://github.com/DanyAxeDev/HEIConverter.git
cd HEIConverter
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## 🧪 Funcionalidades

- Conversão de imagens .heic para .jpeg.

## 📡 Rotas da API

- `/converter`:

Json de envio
```bash
{
  base64: AAAA...
}
```

Json de retorno
```bash
{
  jpegBase64: /9j/...
}
```
