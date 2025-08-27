# 让我创建一个适合您当前情况的完整脚本
# 这个脚本会在当前目录下创建完整的项目结构

import os
import sys

from pathlib import Path

def create_jupyter_book_project():
    """创建完整的Jupyter Book + MyBinder项目"""

    print("🚀 开始创建Jupyter Book项目结构...")

    # 获取当前目录作为项目根目录
    project_root = Path.cwd()
    print(f"📁 项目根目录: {project_root}")

    # 创建目录结构
    directories = [
        "content",
        "content/chapter04",
        "content/chapter07",
        "content/chapter08",
        "assets/images",
        "assets/data",
        "assets/css",
        "scripts",
        ".github/workflows"
    ]

    for dir_path in directories:
        full_path = project_root / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 创建目录: {dir_path}")

    # 1. _config.yml
    config_content = """title: "大语言模型经济学指南"
author: "douzi132"
logo: assets/images/logo.png

execute:
  execute_notebooks: cache
  cache: ""
  exclude_patterns: []
  timeout: 120

launch_buttons:
  binderhub_url: "https://mybinder.org"
  colab_url: "https://colab.research.google.com"

repository:
  url: https://github.com/douzi132/llm-economics-guide
  path_to_book: ""
  branch: main

html:
  use_repository_button: true
  use_issues_button: true
  use_edit_page_button: true
  navbar_number_sections: false
  announcement: "🚀 本教程提供交互式代码环境，点击右上角按钮在线运行！"

parse:
  myst_enable_extensions:
    - colon_fence
    - deflist
    - linkify
    - substitution

sphinx:
  config:
    html_theme_options:
      repository_url: https://github.com/douzi132/llm-economics-guide
      use_repository_button: true
"""

    # 2. _toc.yml
    toc_content = """format: jb-book
root: content/intro
title: "大语言模型经济学指南"

chapters:
- file: content/chapter04/index
  title: "第4章：通义千问API实战"
  sections:
  - file: content/chapter04/api_basics
    title: "4.1 API基础使用"
  - file: content/chapter04/performance_test
    title: "4.2 性能测试与分析"
  - file: content/chapter04/cost_analysis
    title: "4.3 成本分析与优化"

- file: content/chapter07/index
  title: "第7章：本地部署方案"
  sections:
  - file: content/chapter07/local_setup
    title: "7.1 本地环境搭建"
  - file: content/chapter07/performance_optimization
    title: "7.2 性能优化策略"

- file: content/chapter08/index
  title: "第8章：应用开发实战"
  sections:
  - file: content/chapter08/langchain_integration
    title: "8.1 LangChain集成"
  - file: content/chapter08/rag_system
    title: "8.2 RAG系统开发"
"""

    # 3. requirements.txt
    requirements_content = """jupyter-book>=0.15.1
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
requests>=2.25.0
openai>=1.0.0
langchain>=0.1.0
streamlit>=1.28.0
gradio>=4.0.0
dashscope>=1.14.0
"""

    # 4. runtime.txt
    runtime_content = "python-3.9"

    # 5. postBuild
    postbuild_content = """#!/bin/bash
# MyBinder构建后脚本
pip install --upgrade pip
jupyter-book build .
"""

    # 6. README.md
    readme_content = """# 大语言模型经济学指南

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/douzi132/llm-economics-guide/main)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green)](https://douzi132.github.io/llm-economics-guide/)

## 📖 项目简介

这是一个交互式的大语言模型经济学教程，涵盖API使用、本地部署、成本分析等实用内容。

## 🚀 快速开始

### 在线运行
- 点击上方 [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/douzi132/llm-economics-guide/main) 按钮
- 无需安装，直接在浏览器中运行所有代码

### 本地运行
```bash
git clone https://github.com/douzi132/llm-economics-guide.git
cd llm-economics-guide
pip install -r requirements.txt
jupyter-book build .
```

## 📚 内容目录

- **第4章：通义千问API实战**
  - API基础使用与配置
  - 性能测试与基准分析
  - 成本计算与优化策略

- **第7章：本地部署方案**
  - 环境搭建与配置
  - 性能优化技巧

- **第8章：应用开发实战**
  - LangChain框架集成
  - RAG系统开发实践

## 🛠️ 技术栈

- **文档构建**: Jupyter Book
- **在线运行**: MyBinder
- **自动部署**: GitHub Actions
- **主要库**: pandas, matplotlib, langchain, streamlit

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！
"""

    # 7. GitHub Actions workflow
    workflow_content = """name: Build and Deploy Jupyter Book

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install --upgrade pip
        pip install -r requirements.txt

    - name: Build book
      run: |
        jupyter-book build .

    - name: Deploy to GitHub Pages
      if: github.ref == 'refs/heads/main'
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./_build/html
"""

    # 8. 示例内容文件
    intro_content = """# 欢迎来到大语言模型经济学指南

```{note}
本教程提供完全交互式的学习体验。点击右上角的火箭图标选择运行环境！
```

## 🎯 学习目标

通过本教程，您将学会：

1. **API经济学分析** - 理解不同API的成本效益
2. **本地部署策略** - 掌握自建模型的经济考量  
3. **实际应用开发** - 构建真实的LLM应用

## 🚀 交互式体验

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/douzi132/llm-economics-guide/main)

点击上方按钮，立即开始交互式学习！

## 📊 内容预览

```{tableofcontents}
```

---

**准备好开始了吗？** 让我们从第4章的API实战开始吧！
"""

    # 创建所有文件
    files_to_create = {
        "_config.yml": config_content,
        "_toc.yml": toc_content,
        "requirements.txt": requirements_content,
        "runtime.txt": runtime_content,
        "postBuild": postbuild_content,
        "README.md": readme_content,
        ".github/workflows/deploy.yml": workflow_content,
        "content/intro.md": intro_content,
    }

    # 写入文件
    for filename, content in files_to_create.items():
        file_path = project_root / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 创建文件: {filename}")

    # 创建示例notebook文件
    sample_notebooks = {
        "content/chapter04/index.md": """# 第4章：通义千问API实战

本章将深入探讨通义千问API的实际应用，包括基础使用、性能测试和成本分析。

## 本章内容

```{tableofcontents}
```
""",

        "content/chapter04/api_basics.ipynb": """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4.1 通义千问API基础使用\\n",
    "\\n",
    "本节将介绍如何使用通义千问API进行基本的文本生成任务。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 安装必要的库\\n",
    "!pip install dashscope requests\\n",
    "\\n",
    "import dashscope\\n",
    "import os\\n",
    "from dashscope import Generation\\n",
    "import json"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## API配置\\n",
    "\\n",
    "首先需要配置API密钥："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 设置API密钥\\n",
    "# 注意：在实际使用中，请将API密钥设置为环境变量\\n",
    "dashscope.api_key = 'your-api-key-here'\\n",
    "\\n",
    "print('API配置完成！')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}"""
    }

    # 创建notebook文件
    for filename, content in sample_notebooks.items():
        file_path = project_root / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 创建示例文件: {filename}")

    print("\\n🎉 项目创建完成！")
    print("\\n📋 下一步操作：")
    print("1. git add .")
    print("2. git commit -m 'Initial commit: Complete Jupyter Book setup'")
    print("3. git push origin main")
    print("\\n🌐 推送后访问: https://douzi132.github.io/llm-economics-guide/")

if __name__ == "__main__":
    create_jupyter_book_project()
