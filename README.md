# 🖼️ Text-to-Image Generator Powered by ComfyUI

Unlock the power of **AI-driven creativity** with this **Text-to-Image Generator**! Built on **Stable Diffusion** and enhanced by the modular and intuitive **ComfyUI**, this project allows users to seamlessly convert textual descriptions into stunning visuals. Whether you’re an artist, designer, or enthusiast, this tool empowers you to bring your ideas to life with minimal effort and maximum creativity.

---

## 🌟 Key Features

- **ComfyUI Integration**: Fully integrates the modular, node-based **ComfyUI** for complete workflow flexibility.
- **Text-to-Image Conversion**: Generate high-quality images directly from textual descriptions.
- **Customizable Parameters**: Fine-tune settings like resolution, image style, sampling methods, and more.
- **Real-Time Previews**: Get instant feedback on your generated images as you adjust inputs.
- **Node-Based Workflow**: Design and save modular workflows tailored to your specific requirements.
- **Custom Nodes Support**: Extend functionality by adding your own custom nodes.
- **Multi-Model Support**: Utilize different `.ckpt` or `.safetensors` models for diverse artistic outcomes.

---

## 🛠️ Technologies Used

- **Stable Diffusion**: State-of-the-art text-to-image generation model.
- **ComfyUI**: An advanced GUI offering modular and node-based workflow design.
- **Python**: The backbone for integrating Stable Diffusion with ComfyUI and managing the generation process.

---

## 🚀 Getting Started

### Prerequisites

1. **Operating System**:
   - Windows, macOS, or Linux.
2. **Python**:
   - Python 3.10.x is required for Stable Diffusion compatibility.
3. **GPU**:
   - A CUDA-compatible GPU is highly recommended for optimal performance.
4. **Stable Diffusion Model**:
   - Download `.ckpt` or `.safetensors` model files from trusted sources and place them in the appropriate directory.

---

### Installation & Setup

Follow these steps to set up and run the Text-to-Image Generator:

#### 1. Clone the Repository
   ```bash
   git clone https://github.com/divyanshi116/text-to-image-generator.git
   cd text-to-image-generator
   ```

#### 2. Set Up a Virtual Environment (Optional but Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

#### 3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

#### 4. Download Stable Diffusion Models
   - Place your `.ckpt` or `.safetensors` model files in the `models/` directory.

#### 5. Run the Application
   ```bash
   python app.py
   ```

#### 6. Access the Interface
   - Open your web browser and navigate to:
     ```
     http://127.0.0.1:8188
     ```

---

## 🖥️ Using the Application

1. **Enter Text Prompt**:
   - Provide a textual description of the image you want to generate.

2. **Adjust Parameters**:
   - Customize settings like resolution, sampling method, and style to achieve the desired output.

3. **Generate Images**:
   - Hit the "Generate" button to start the image creation process.

4. **Save & Export**:
   - Download the generated image for your projects.

5. **Workflow Management**:
   - Use ComfyUI’s node-based design to create and save customizable workflows for future use.

---

## 📂 Directory Structure

- **`models/`**: Store your `.ckpt` or `.safetensors` files here.
- **`custom_nodes/`**: Add custom Python scripts to extend ComfyUI’s functionality.
- **`workflows/`**: Save and manage node-based workflows for reuse.
- **`outputs/`**: Access your generated images here.

---

## 🔧 ComfyUI: Key Component of the Project

### What is ComfyUI?

**ComfyUI** is a powerful, node-based graphical user interface for Stable Diffusion. It provides users with unparalleled flexibility to design, customize, and manage workflows for generating images.

### ComfyUI Setup & Installation

1. **Clone the ComfyUI Repository**
   ```bash
   git clone https://github.com/comfyanonymous/ComfyUI.git
   cd ComfyUI
   ```

2. **Set Up a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Stable Diffusion Models**
   - Place your `.ckpt` or `.safetensors` files in the `models/` directory.

5. **Run ComfyUI**
   ```bash
   python main.py
   ```
   - Navigate to `http://127.0.0.1:8188` in your browser to access the interface.

---

### Advanced Features of ComfyUI

- **Node-Based Workflow**:
  - Drag and drop nodes to create a custom image generation pipeline.
  - Visualize and modify every step of the process.

- **Custom Nodes**:
  - Add your own nodes to introduce new functionalities.
  - Simply place the scripts in the `custom_nodes/` directory.

- **Save & Load Workflows**:
  - Export workflows for reuse or share them with collaborators.

---

## ✨ Example Use Cases

- **Art Creation**: Generate unique artworks from textual descriptions.
- **Design Inspiration**: Use AI to brainstorm visual ideas for creative projects.
- **Learning Tool**: Explore the capabilities of Stable Diffusion and ComfyUI.
- **Storytelling**: Create illustrations for your stories, blogs, or presentations.

---

## 🎯 Future Enhancements

- **Multi-Style Models**: Support for multiple pre-trained styles for diverse outputs.
- **Interactive Editing**: Introduce features for real-time image editing.
- **Cloud Integration**: Enable cloud-based image generation for users without GPUs.
- **Mobile Compatibility**: Develop a mobile-friendly version of the application.

---

## 🤝 Contributing

Contributions are welcome! Whether it’s adding features, fixing bugs, or improving documentation, feel free to fork the repository and open a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For any questions, suggestions, or feedback, feel free to reach out to [divyanshi116](https://github.com/divyanshi116). 🚀
