# ✨ TexttoImage ✨

TexttoImage is a Python-based project that transforms your text prompts into stunning images! 🚀 Built with a robust workflow and an intuitive interface, it’s your go-to solution for creative text-to-image generation.

---

## 🌟 Features

- 🖼️ **Text-to-Image Generation**: Convert your imagination into visuals effortlessly.
- ⚙️ **Customizable Parameters**: Fine-tune seed values, steps, and more for personalized outputs.
- 🔄 **Real-Time Image Updates**: Automatically fetches the latest generated image.
- 🖥️ **User-Friendly Interface**: Gradio-powered for seamless usage.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/divyanshi116/TexttoImage.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TexttoImage
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. Run the application:
   ```bash
   python index.py
   ```
2. Open the provided Gradio link in your browser. 🌐
3. Enter a text prompt in the input box and generate your image! 🎨

---

## 🔧 Workflow Configuration

The image generation process is powered by the `workflow (1).json` file, which defines the parameters and structure of the generation pipeline. Key components include:

- ✏️ **Prompt Settings**: Define positive and negative prompts to refine the results.
- 📦 **Model Loader**: Load the desired model checkpoint for image generation.
- 🎛️ **Sampler and Scheduler**: Customize sampling techniques and scheduling for optimized outputs.
- 🖼️ **Output Settings**: Configure image dimensions and batch size.

---

## 📂 Project Structure

- `index.py`: Main script that initializes the Gradio interface and handles text-to-image generation.
- `workflow (1).json`: Configuration file for the image generation workflow.

---

## 🎉 Example

1. Enter a text prompt like:
   ```
   beautiful scenery nature glass bottle landscape, purple galaxy bottle
   ```
2. The application will generate an image based on the prompt and display it in the Gradio interface. 🌟

---

## 📋 Dependencies

- 🐍 Python 3.x
- 🌐 Gradio
- 🖼️ PIL (Pillow)
- 🔗 Requests

---

## 🙌 Acknowledgments

This project integrates various tools and libraries to deliver a seamless experience for generating text-based images. Special thanks to the open-source community for their invaluable resources. ❤️

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! 🚀 Feel free to submit issues or pull requests to improve the project.

---

## 📧 Contact

Have questions or feedback? Reach out to [divyanshi116](https://github.com/divyanshi116). 💬
