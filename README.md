# Recomendador de Notícias - Datathon FIAP & Globo

Este projeto tem como objetivo desenvolver um algoritmo/modelo de recomendação de notícias capaz de lidar com o problema de **cold start**. O desafio faz parte do **Datathon FIAP & Globo** e utiliza a base de dados de notícias do **G1**.

## 📌 Objetivo

Criar um sistema de recomendação que:

- Sugira notícias relevantes para os usuários com base em seu histórico de leitura.
- Considere a similaridade entre notícias e perfis de usuários.
- Minimize o impacto do problema de **cold start**, recomendando conteúdos mesmo para novos usuários.

## 🔧 Como Desenvolver

O ambiente de desenvolvimento está configurado para ser utilizado com **Dev Containers** no **Visual Studio Code**.

### **Passos para configurar o ambiente**

1. **Instale o Visual Studio Code** e a extensão **Dev Containers**.
2. **Clone o repositório**
3. **Abra o projeto no VS Code**.
4. **Abra o Dev Container** (o VS Code perguntará automaticamente ou vá até `View > Command Palette > Dev Containers: Reopen in Container`).
5. O Dev Container irá **baixar automaticamente a base de dados inicial** na pasta `data/raw`, caso ela ainda não esteja disponível.

Após esses passos, o ambiente estará pronto para desenvolvimento! 🚀
