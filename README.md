# Learning from mistake — Translation of Indigenous Languages

This project explores the use of Large Language Models (LLMs) for translating Taiwan's low-resource indigenous languages. We compare various prompting methods to identify the most effective strategy for improving translation quality through error reflection.

## 🎯 Motivation & Purpose

### Motivation
- LLMs have demonstrated strong capabilities in translation tasks.
- However, research on extremely low-resource languages (e.g., Taiwan's indigenous languages) remains limited.

### Purpose
- To investigate different prompting techniques.
- To determine which approach performs best in translating indigenous languages.

## 🧾 Corpus Description

Source: [族語 e 樂園 (Klokah)](https://web.klokah.tw/)

Corpus includes:
- Sediq Truku (450 sentences)
- Nanshi Amis (450 sentences)
- Wanta Atayal (450 sentences)

Data is split into:
- Training set (350 sentences)
- Test set (100 sentences)

## 🔍 Methods

We tested and compared the following prompting strategies:
- **KNN-Prompting**
- **CoT (Chain-of-Thought) Prompting**
- **LFM (Learning From Mistakes) Prompting**

Multiple LLMs (such as GPT-3.5 and GPT-4) were used to evaluate consistency across models.

## 📊 Experimental Results & Discussion

- **CoT Prompting** achieved the best translation accuracy.
- **LFM Prompting** showed better performance in structure and language logic.
- All tested LLMs showed a consistent performance trend across different prompt strategies.

## 💡 Learning From Mistakes (LFM)

The LFM method incorporates error reflection, allowing the model to adjust its translation strategy. This is especially effective for low-resource languages with unique grammar and structure.

## 🧠 Conclusion

- Prompt design significantly influences translation results.
- LFM Prompting has potential for structured and accurate output.
- Cultural and linguistic knowledge is essential when dealing with indigenous language translation.

## ⚙️ Technical Details

- Platforms used: OpenAI, Hugging Face
- LLMs: GPT-3.5, GPT-4 (and others)
- Programming language: Python (assumed)

## 👥 Contributors

- Chi-Yi Lin
- Yun Hefeng  
- Supervisor: Prof. Yao-Chung Fan

## 📄 License

This project is licensed under the MIT License.

---

📫 **Contact**  
Feel free to open an issue or contact us if you have questions!

