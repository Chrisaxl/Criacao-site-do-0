# 📸 INSTRUÇÕES PARA ADICIONAR IMAGENS

## 🖼️ Imagens Necessárias

O site está configurado para usar as seguintes imagens. Você precisa adicionar essas imagens na mesma pasta do `index.html`:

### 1. **logo.png** - Logo da Empresa
- **Localização:** No menu fixo (topo da página)
- **Tamanho recomendado:** 40x40 pixels ou proporcional
- **Formato:** PNG (com fundo transparente é melhor)
- **Onde colocar:** Na mesma pasta do `index.html`

### 2. **banner.jpg** - Banner Principal
- **Localização:** Seção inicial (hero banner)
- **Tamanho recomendado:** 1200x400 pixels
- **Formato:** JPG ou PNG
- **Onde colocar:** Na mesma pasta do `index.html`

### 3. **sobre-nos.jpg** - Imagem da Seção "Sobre Nós"
- **Localização:** Seção "Sobre Nós!"
- **Tamanho recomendado:** 600x400 pixels
- **Formato:** JPG ou PNG
- **Onde colocar:** Na mesma pasta do `index.html`

### 4. **Imagens dos Produtos:**
- **smartphone.jpg** - Para o card "Smartphone Premium"
- **notebook.jpg** - Para o card "Notebook Gamer"
- **fones.jpg** - Para o card "Fones Bluetooth"
- **tablet.jpg** - Para o card "Tablet Pro"
- **smartwatch.jpg** - Para o card "Smartwatch Fitness"
- **teclado.jpg** - Para o card "Teclado Mecânico RGB"
- **Tamanho recomendado:** 400x200 pixels cada
- **Formato:** JPG ou PNG
- **Onde colocar:** Na mesma pasta do `index.html`

---

## 🔧 Como Adicionar Suas Próprias Imagens

### Opção 1: Usar Imagens Locais
1. Coloque suas imagens na mesma pasta do `index.html`
2. Renomeie as imagens exatamente como os nomes acima
3. Pronto! O site carregará automaticamente

### Opção 2: Usar URLs de Imagens Online
Se você quiser usar imagens de sites como Unsplash, Pexels, etc:

1. Abra o arquivo `index.html`
2. Procure por: `src="nome-da-imagem.jpg"`
3. Substitua por: `src="https://url-da-imagem.com/imagem.jpg"`

**Exemplo:**
```html
<!-- Antes -->
<img src="banner.jpg" alt="Banner TECNOFANJOS">

<!-- Depois -->
<img src="https://images.unsplash.com/photo-1234567890" alt="Banner TECNOFANJOS">
```

---

## 🎨 Sites para Baixar Imagens Gratuitas

- **Unsplash:** https://unsplash.com
- **Pexels:** https://www.pexels.com
- **Pixabay:** https://pixabay.com
- **Freepik:** https://www.freepik.com

---

## ⚠️ Importante

- Se você não adicionar as imagens, o navegador mostrará um ícone de imagem quebrada
- As imagens são opcionais - o site funcionará sem elas
- Certifique-se de que os nomes dos arquivos estão corretos (maiúsculas/minúsculas importam)
- Para melhor performance, use imagens otimizadas (comprimidas)

---

## 📝 Nota sobre Placeholders

Se você quiser usar imagens placeholder temporárias enquanto prepara as imagens reais, pode usar:

```
https://via.placeholder.com/1200x400/1e3a8a/ffffff?text=TECNOFANJOS
```

Substitua os números conforme necessário:
- `1200x400` = largura x altura
- `1e3a8a` = cor de fundo (azul)
- `ffffff` = cor do texto (branco)
- `text=TECNOFANJOS` = texto a exibir

