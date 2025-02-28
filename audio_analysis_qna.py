{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DhguEVZM_tbV",
        "outputId": "04cb05cb-5461-4bc1-e8d3-ac7e9d84bc32"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "nSzalr6pAp2D"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "\n",
        "with open('/content/drive/MyDrive/LLM_Projects/.bashrc') as file:\n",
        "    for line in file:\n",
        "        if line.startswith('export '):\n",
        "            var, value = line[len('export '):].strip().split('=')\n",
        "            os.environ[var] = value\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-xn1VQrQcAv2",
        "outputId": "28978ba3-0086-47d7-ba17-a27942b27ed7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Collecting git+https://github.com/openai/whisper.git\n",
            "  Cloning https://github.com/openai/whisper.git to /tmp/pip-req-build-preghnkx\n",
            "  Running command git clone --filter=blob:none --quiet https://github.com/openai/whisper.git /tmp/pip-req-build-preghnkx\n",
            "  Resolved https://github.com/openai/whisper.git to commit ba3f3cd54b0e5b8ce1ab3de13e32122d0d5f98ab\n",
            "  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: numba in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (0.58.1)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (1.25.2)\n",
            "Requirement already satisfied: torch in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (2.3.0+cu121)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (4.66.4)\n",
            "Requirement already satisfied: more-itertools in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (10.1.0)\n",
            "Collecting tiktoken (from openai-whisper==20231117)\n",
            "  Downloading tiktoken-0.7.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m12.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: triton<3,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (2.3.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from triton<3,>=2.0.0->openai-whisper==20231117) (3.14.0)\n",
            "Requirement already satisfied: llvmlite<0.42,>=0.41.0dev0 in /usr/local/lib/python3.10/dist-packages (from numba->openai-whisper==20231117) (0.41.1)\n",
            "Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken->openai-whisper==20231117) (2024.5.15)\n",
            "Requirement already satisfied: requests>=2.26.0 in /usr/local/lib/python3.10/dist-packages (from tiktoken->openai-whisper==20231117) (2.31.0)\n",
            "Requirement already satisfied: typing-extensions>=4.8.0 in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (4.12.2)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (1.12.1)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (3.1.4)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (2023.6.0)\n",
            "Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (23.7 MB)\n",
            "Collecting nvidia-cuda-runtime-cu12==12.1.105 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (823 kB)\n",
            "Collecting nvidia-cuda-cupti-cu12==12.1.105 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (14.1 MB)\n",
            "Collecting nvidia-cudnn-cu12==8.9.2.26 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl (731.7 MB)\n",
            "Collecting nvidia-cublas-cu12==12.1.3.1 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl (410.6 MB)\n",
            "Collecting nvidia-cufft-cu12==11.0.2.54 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl (121.6 MB)\n",
            "Collecting nvidia-curand-cu12==10.3.2.106 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl (56.5 MB)\n",
            "Collecting nvidia-cusolver-cu12==11.4.5.107 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl (124.2 MB)\n",
            "Collecting nvidia-cusparse-cu12==12.1.0.106 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl (196.0 MB)\n",
            "Collecting nvidia-nccl-cu12==2.20.5 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_nccl_cu12-2.20.5-py3-none-manylinux2014_x86_64.whl (176.2 MB)\n",
            "Collecting nvidia-nvtx-cu12==12.1.105 (from torch->openai-whisper==20231117)\n",
            "  Using cached nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (99 kB)\n",
            "Collecting nvidia-nvjitlink-cu12 (from nvidia-cusolver-cu12==11.4.5.107->torch->openai-whisper==20231117)\n",
            "  Downloading nvidia_nvjitlink_cu12-12.5.40-py3-none-manylinux2014_x86_64.whl (21.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m21.3/21.3 MB\u001b[0m \u001b[31m16.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (2024.6.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch->openai-whisper==20231117) (2.1.5)\n",
            "Requirement already satisfied: mpmath<1.4.0,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch->openai-whisper==20231117) (1.3.0)\n",
            "Building wheels for collected packages: openai-whisper\n",
            "  Building wheel for openai-whisper (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for openai-whisper: filename=openai_whisper-20231117-py3-none-any.whl size=802826 sha256=e18e5a43cb41dda0e686733a270917d0246532a46c4e057c307cc32bd7e88828\n",
            "  Stored in directory: /tmp/pip-ephem-wheel-cache-w__5_zx1/wheels/8b/6c/d0/622666868c179f156cf595c8b6f06f88bc5d80c4b31dccaa03\n",
            "Successfully built openai-whisper\n",
            "Installing collected packages: nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, tiktoken, nvidia-cusparse-cu12, nvidia-cudnn-cu12, nvidia-cusolver-cu12, openai-whisper\n",
            "Successfully installed nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.20.5 nvidia-nvjitlink-cu12-12.5.40 nvidia-nvtx-cu12-12.1.105 openai-whisper-20231117 tiktoken-0.7.0\n",
            "Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Get:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]\n",
            "Get:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]\n",
            "Get:4 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease [3,626 B]\n",
            "Get:5 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  InRelease [1,581 B]\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:7 https://ppa.launchpadcontent.net/c2d4u.team/c2d4u4.0+/ubuntu jammy InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/graphics-drivers/ppa/ubuntu jammy InRelease\n",
            "Hit:10 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Get:11 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ Packages [55.4 kB]\n",
            "Get:12 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64  Packages [927 kB]\n",
            "Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,391 kB]\n",
            "Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,183 kB]\n",
            "Get:15 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,092 kB]\n",
            "Get:16 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [1,917 kB]\n",
            "Fetched 7,827 kB in 1s (7,681 kB/s)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "49 packages can be upgraded. Run 'apt list --upgradable' to see them.\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "ffmpeg is already the newest version (7:4.4.2-0ubuntu0.22.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 49 not upgraded.\n",
            "Collecting pytube\n",
            "  Downloading pytube-15.0.0-py3-none-any.whl (57 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.6/57.6 kB\u001b[0m \u001b[31m2.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pytube\n",
            "Successfully installed pytube-15.0.0\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m898.7/898.7 kB\u001b[0m \u001b[31m11.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m43.2/43.2 kB\u001b[0m \u001b[31m8.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.0/2.0 MB\u001b[0m \u001b[31m24.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.5/79.5 kB\u001b[0m \u001b[31m13.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.5/58.5 kB\u001b[0m \u001b[31m10.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.1/48.1 kB\u001b[0m \u001b[31m8.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m51.4/51.4 kB\u001b[0m \u001b[31m9.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m119.1/119.1 kB\u001b[0m \u001b[31m19.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m760.1/760.1 kB\u001b[0m \u001b[31m35.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m101.7/101.7 kB\u001b[0m \u001b[31m19.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.1/50.1 kB\u001b[0m \u001b[31m9.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m868.8/868.8 kB\u001b[0m \u001b[31m40.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m812.2/812.2 kB\u001b[0m \u001b[31m45.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m117.0/117.0 kB\u001b[0m \u001b[31m19.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m380.1/380.1 kB\u001b[0m \u001b[31m37.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m59.6/59.6 kB\u001b[0m \u001b[31m11.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m233.4/233.4 kB\u001b[0m \u001b[31m34.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m117.8/117.8 kB\u001b[0m \u001b[31m17.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m78.6/78.6 kB\u001b[0m \u001b[31m14.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m526.7/526.7 kB\u001b[0m \u001b[31m53.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for antlr4-python3-runtime (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for docopt (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for julius (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting groq\n",
            "  Downloading groq-0.9.0-py3-none-any.whl (103 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m103.5/103.5 kB\u001b[0m \u001b[31m3.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting gTTS\n",
            "  Downloading gTTS-2.5.1-py3-none-any.whl (29 kB)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from groq) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from groq) (1.7.0)\n",
            "Collecting httpx<1,>=0.23.0 (from groq)\n",
            "  Downloading httpx-0.27.0-py3-none-any.whl (75 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m75.6/75.6 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from groq) (2.7.3)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from groq) (1.3.1)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from groq) (4.12.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from gTTS) (2.31.0)\n",
            "Requirement already satisfied: click<8.2,>=7.1 in /usr/local/lib/python3.10/dist-packages (from gTTS) (8.1.7)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->groq) (3.7)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->groq) (1.2.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->groq) (2024.6.2)\n",
            "Collecting httpcore==1.* (from httpx<1,>=0.23.0->groq)\n",
            "  Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.9/77.9 kB\u001b[0m \u001b[31m6.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->groq)\n",
            "  Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m5.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->groq) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.18.4 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->groq) (2.18.4)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (3.3.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (2.0.7)\n",
            "Installing collected packages: h11, httpcore, gTTS, httpx, groq\n",
            "Successfully installed gTTS-2.5.1 groq-0.9.0 h11-0.14.0 httpcore-1.0.5 httpx-0.27.0\n"
          ]
        }
      ],
      "source": [
        "!pip install git+https://github.com/openai/whisper.git #install whisper getting from github\n",
        "!sudo apt update && sudo apt install ffmpeg #ffmpeg allows us to work with audio and video files\n",
        "!pip install pytube\n",
        "!pip install   pydub -qq\n",
        "!pip install pyannote.audio -qq\n",
        "!pip install  transformers torch  numpy  -qq\n",
        "!pip install groq gTTS\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PBYECz_nBHMj",
        "outputId": "63d440bd-8518-417e-b48f-e4c66a489e10"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m131.2/131.2 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m130.2/130.2 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install elevenlabs -qq"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HNeMY4SaMmBG"
      },
      "source": [
        "**Task 1:Generating Q&A using GROQ from llama3 and outputting audio**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "iCk-7dw3_xPR"
      },
      "outputs": [],
      "source": [
        "from pytube import YouTube\n",
        "\n",
        "def download_youtube_audio(video_url):\n",
        "    yt = YouTube(video_url)\n",
        "    stream = yt.streams.filter(only_audio=True).first()\n",
        "    audio_file_path = yt.title + \".mp3\"\n",
        "\n",
        "    stream.download(filename=audio_file_path)\n",
        "\n",
        "    return audio_file_path\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "Z7-TANnWb_7S"
      },
      "outputs": [],
      "source": [
        "video_url = \"https://youtu.be/Own9MiaP57o?si=6plLESUP5YD_1hBg\"\n",
        "audio_file_path = download_youtube_audio(video_url)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4-opUpZoAld9",
        "outputId": "fd5a5815-978b-42c4-92ad-3ff002637448"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "100%|█████████████████████████████████████| 1.42G/1.42G [05:18<00:00, 4.79MiB/s]\n",
            "[00:00.000 --> 00:06.640]  iOS 18 is a big release that delivers more ways to customize your iPhone, stay connected,\n",
            "[00:06.640 --> 00:11.200]  and relive special moments. You can already customize your home screen with your favorite\n",
            "[00:11.200 --> 00:17.920]  wallpaper, apps, and widgets, letting your personality shine through. And now, your app\n",
            "[00:17.920 --> 00:24.960]  icons and widgets can add even more. I have this photo I love as my wallpaper, and now I can\n",
            "[00:24.960 --> 00:30.400]  continue to enjoy it when I unlock my iPhone, because I can arrange my apps and widgets to\n",
            "[00:30.400 --> 00:37.200]  frame it perfectly. I can select them all and easily place them along the bottom, right above\n",
            "[00:37.200 --> 00:45.840]  the dock, for easy access, or even off to the side. We have an awesome new look for app icons\n",
            "[00:45.840 --> 00:54.800]  when we go into dark mode. Let's turn it on. Isn't that cool? Now, in addition to this new dark look,\n",
            "[00:55.040 --> 01:02.320]  there are even more new ways to adjust how they look. I can bring up a new customization sheet,\n",
            "[01:02.320 --> 01:10.080]  and now I can tint them all with color. iOS suggests a tint color that complements my wallpaper,\n",
            "[01:10.640 --> 01:13.920]  or I can select any other color I want.\n",
            "[01:18.400 --> 01:24.080]  Now they really pop. Another key part of personalizing iOS is about keeping you in\n",
            "[01:24.080 --> 01:30.400]  control of your privacy. So this year, we're giving you a new way to protect sensitive apps\n",
            "[01:30.400 --> 01:36.000]  and the information inside them by letting you lock an app. When you choose to lock an app,\n",
            "[01:36.000 --> 01:41.120]  if someone else tries to tap it, they will be required to authenticate using Face ID,\n",
            "[01:41.120 --> 01:47.440]  Touch ID, or your passcode. And information from inside the app won't appear in other places across\n",
            "[01:47.440 --> 01:52.720]  the system, like in search and notifications, so others won't inadvertently see sensitive\n",
            "[01:52.720 --> 01:58.160]  information. There may also be occasions when you want to hide an app that you don't want others to\n",
            "[01:58.160 --> 02:04.880]  know is installed in your device. For example, say you use a professional-grade spatial capture app\n",
            "[02:04.880 --> 02:09.840]  to track your different hairstyles. I mean, that's just good science, right? Well, anyway,\n",
            "[02:09.840 --> 02:17.040]  say you use this app, but you don't want anyone else to know. Well, now you can hide it and put\n",
            "[02:17.040 --> 02:23.120]  it in a new hidden apps folder that's locked. We have big enhancements to the apps we use to stay\n",
            "[02:23.120 --> 02:31.120]  connected, starting with Messages. To tell you more, here's Ronik. In iOS 18, we're giving you\n",
            "[02:31.120 --> 02:38.160]  all new ways to express yourself and stay connected. Let's start with Tapbacks. Tapbacks\n",
            "[02:38.160 --> 02:44.000]  are one of the most popular ways to express yourself in Messages, and people love them. This\n",
            "[02:44.000 --> 02:49.680]  is a huge year for Tapbacks. We've not only redesigned your favorites, we're now giving you\n",
            "[02:49.680 --> 02:56.400]  limitless ways to express yourself by letting you tap back with any emoji or sticker. Next,\n",
            "[02:56.400 --> 03:01.040]  we're bringing one of your most requested features to Messages. When you don't want to forget to send\n",
            "[03:01.040 --> 03:06.720]  that friendly reminder or birthday text in the morning, you can schedule your message to send\n",
            "[03:06.720 --> 03:13.520]  later. We're also giving you more ways to express your tone with Text Formatting. Bold, italicize,\n",
            "[03:13.520 --> 03:18.880]  underline, or strike through any text. And when formatting is not enough, we're introducing a\n",
            "[03:18.880 --> 03:24.240]  new way to visually amplify your messages with Text Effects. Whether you want to emphasize some\n",
            "[03:24.240 --> 03:30.960]  major news, bring your emoji to life, or you're just blown away by a stunning photo, you can\n",
            "[03:30.960 --> 03:37.040]  express yourself in all new ways with Text Effects. Some words and phrases automatically\n",
            "[03:37.040 --> 03:43.760]  surface a suggestion, so you can quickly select one and send it. And you can also add one of the\n",
            "[03:43.760 --> 03:50.480]  many new effects to any text. There's a new way to stay connected whenever you don't have Wi-Fi or\n",
            "[03:50.480 --> 03:55.760]  cellular service. We're using the same groundbreaking technology that gave us Emergency SOS\n",
            "[03:55.760 --> 04:02.480]  via satellite to bring you messages via satellite. Now, you can use the satellite capabilities on\n",
            "[04:02.480 --> 04:07.280]  iPhone 14 and later to connect to satellites hundreds of miles above the earth to text your\n",
            "[04:07.280 --> 04:11.360]  friends and family when you're off the grid. Once you're connected, you'll be able to use\n",
            "[04:11.360 --> 04:17.760]  key iMessage features like sending and receiving messages, emoji, and tap backs. Because iMessage\n",
            "[04:17.760 --> 04:24.000]  was built to protect your privacy, iMessages sent over satellite are end-to-end encrypted.\n",
            "[04:24.000 --> 04:29.760]  And if you need to text people not on iMessage, we're supporting SMS messaging via satellite too.\n",
            "[04:29.760 --> 04:36.800]  Continuing on our journey to replace your physical wallet, we're introducing Tap to Cash, a quick and\n",
            "[04:36.800 --> 04:42.800]  private way to exchange Apple Cash without sharing phone numbers or email addresses. With Tap to Cash,\n",
            "[04:42.800 --> 04:48.240]  you can pay someone back for dinner just by holding your phones together. We're adding two\n",
            "[04:48.240 --> 04:53.360]  new ways to pay with Apple Pay Online, giving customers around the world the ability to redeem\n",
            "[04:53.360 --> 04:59.920]  rewards and access installments from their banks and card providers. And event tickets are getting\n",
            "[04:59.920 --> 05:05.920]  a beautiful new design and new features, including an all-new event guide combining helpful\n",
            "[05:05.920 --> 05:11.040]  information about the venue with smart recommendations from your favorite Apple apps.\n",
            "[05:11.040 --> 05:18.880]  So that's iOS 18, a big release that brings deeper customization to iPhone, new ways to stay connected\n",
            "[05:18.880 --> 05:26.800]  in messages and mail, enhancements to privacy, and the biggest photos redesign ever, making it even\n",
            "[05:26.800 --> 05:32.720]  easier to relive those special moments. And so much more, including an option for larger icons\n",
            "[05:32.720 --> 05:38.720]  on the home screen, RCS messaging support, and Reminders integration in Calendar.\n",
            "Transcription has been saved to /content/Apple_WWDC_2024_Transcription.txt\n"
          ]
        }
      ],
      "source": [
        "\n",
        "!whisper \"/content/Apple Reveals iOS 18 at WWDC 2024.mp3\" --model medium.en --output_format txt\n",
        "\n",
        "original_output_file = \"/content/Apple Reveals iOS 18 at WWDC 2024.txt\"\n",
        "new_output_file = \"/content/Apple_WWDC_2024_Transcription.txt\"\n",
        "\n",
        "with open(original_output_file, 'r') as file:\n",
        "    transcribed_text = file.read()\n",
        "\n",
        "with open(new_output_file, 'w') as file:\n",
        "    file.write(transcribed_text)\n",
        "\n",
        "print(f\"Transcription has been saved to {new_output_file}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PP1eWS2RAQhy",
        "outputId": "829ec51b-d436-4755-b04e-8c2837ee1cde"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Q&A pairs have been saved to /content/Apple_WWDC_2024_Q_and_A.txt\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "from groq import Groq\n",
        "\n",
        "def get_completion(prompt, model=\"llama3-70b-8192\"):\n",
        "    client = Groq(api_key=os.environ.get(\"GROQ_API_KEY\"))\n",
        "    chat_completion = client.chat.completions.create(\n",
        "        messages=[\n",
        "            {\n",
        "                \"role\": \"user\",\n",
        "                \"content\": prompt,\n",
        "            }\n",
        "        ],\n",
        "        model=model,\n",
        "    )\n",
        "    return chat_completion.choices[0].message.content\n",
        "\n",
        "transcribed_file_path = \"/content/Apple Reveals iOS 18 at WWDC 2024.txt\"\n",
        "\n",
        "with open(transcribed_file_path, 'r') as file:\n",
        "    transcribed_text = file.read()\n",
        "\n",
        "prompt = f\"Create 5 Q&A pairs from the following text. Ensure that each pair includes only the question and the answer. Do not include any introductory phrases, headings, or concluding statements. Each question should be directly related to the content, and each answer should be concise and informative:\\n\\n{transcribed_text}\"\n",
        "\n",
        "q_and_a_text = get_completion(prompt)\n",
        "\n",
        "lines = q_and_a_text.split('\\n')\n",
        "cleaned_q_and_a_text = []\n",
        "for line in lines:\n",
        "    line = line.strip()\n",
        "    if line.startswith(\"Q: \"):\n",
        "        cleaned_q_and_a_text.append(line[3:].strip())\n",
        "    elif line.startswith(\"A: \"):\n",
        "        cleaned_q_and_a_text.append(line[3:].strip())\n",
        "\n",
        "if len(cleaned_q_and_a_text) % 2 != 0:\n",
        "    raise ValueError(\"The number of lines in the Q&A text is not even, indicating a possible mismatch between questions and answers.\")\n",
        "\n",
        "q_and_a_output_file_path = \"/content/Apple_WWDC_2024_Q_and_A.txt\"\n",
        "with open(q_and_a_output_file_path, 'w') as file:\n",
        "    file.write(\"\\n\".join(cleaned_q_and_a_text))\n",
        "\n",
        "print(f\"Q&A pairs have been saved to {q_and_a_output_file_path}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CN78e4ZhA1C5",
        "outputId": "67124ce8-b56a-4357-d4aa-cdd419fe5d53"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Combined Q&A audio saved to: /content/Apple_WWDC_2024_Q_and_A_combined.mp3\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "from io import BytesIO\n",
        "from pydub import AudioSegment\n",
        "from elevenlabs import VoiceSettings\n",
        "from elevenlabs.client import ElevenLabs\n",
        "\n",
        "ELEVENLABS_API_KEY = os.getenv(\"ELEVENLABS_API_KEY\")\n",
        "client = ElevenLabs(api_key=ELEVENLABS_API_KEY)\n",
        "\n",
        "def text_to_speech_stream(text: str, voice_id: str) -> BytesIO:\n",
        "    response = client.text_to_speech.convert(\n",
        "        voice_id=voice_id,\n",
        "        optimize_streaming_latency=\"0\",\n",
        "        output_format=\"mp3_22050_32\",\n",
        "        text=text,\n",
        "        model_id=\"eleven_multilingual_v2\",\n",
        "        voice_settings=VoiceSettings(\n",
        "            stability=0.0,\n",
        "            similarity_boost=1.0,\n",
        "            style=0.0,\n",
        "            use_speaker_boost=True,\n",
        "        ),\n",
        "    )\n",
        "    audio_stream = BytesIO()\n",
        "    for chunk in response:\n",
        "        if chunk:\n",
        "            audio_stream.write(chunk)\n",
        "    audio_stream.seek(0)\n",
        "    return audio_stream\n",
        "\n",
        "\n",
        "with open(q_and_a_output_file_path, 'r') as file:\n",
        "    q_and_a_text = file.read()\n",
        "\n",
        "if not q_and_a_text.strip():\n",
        "    raise ValueError(\"No text found in the Q&A file.\")\n",
        "\n",
        "lines = [line.strip() for line in q_and_a_text.split('\\n') if line.strip()]\n",
        "if len(lines) % 2 != 0:\n",
        "    raise ValueError(\"The number of lines in the Q&A text is not even, indicating a possible mismatch between questions and answers.\")\n",
        "\n",
        "questions = [lines[i] for i in range(0, len(lines), 2)]\n",
        "answers = [lines[i] for i in range(1, len(lines), 2)]\n",
        "\n",
        "question_voice_id = \"21m00Tcm4TlvDq8ikWAM\"\n",
        "answer_voice_id = \"29vD33N1CtxCmqQRPOHJ\"\n",
        "\n",
        "def generate_audio_stream(text, voice_id):\n",
        "    audio_stream = text_to_speech_stream(text, voice_id)\n",
        "    return audio_stream\n",
        "\n",
        "question_audio_streams = [generate_audio_stream(f\" {question}\", question_voice_id) for question in questions]\n",
        "answer_audio_streams = [generate_audio_stream(f\" {answer}\", answer_voice_id) for answer in answers]\n",
        "\n",
        "question_audio = AudioSegment.empty()\n",
        "answer_audio = AudioSegment.empty()\n",
        "\n",
        "combined_audio = AudioSegment.empty()\n",
        "\n",
        "for question_stream, answer_stream in zip(question_audio_streams, answer_audio_streams):\n",
        "    question_segment = AudioSegment.from_file(question_stream)\n",
        "    answer_segment = AudioSegment.from_file(answer_stream)\n",
        "    combined_audio += question_segment\n",
        "    combined_audio += answer_segment\n",
        "\n",
        "audio_output_file_path = \"/content/Apple_WWDC_2024_Q_and_A_combined.mp3\"\n",
        "combined_audio.export(audio_output_file_path, format=\"mp3\")\n",
        "\n",
        "print(f\"Combined Q&A audio saved to: {audio_output_file_path}\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NQ7GshCTMznR"
      },
      "source": [
        "**Task 2: Identifying the number of speakers and gender of the speakers for a given youtube video**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_QROIV4Z4eV1",
        "outputId": "f0099e6e-17a3-4d67-abe7-ceb1b2e72a9a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Audio has been downloaded and converted to WAV format: panel_discussion_audio.wav\n"
          ]
        }
      ],
      "source": [
        "from pytube import YouTube\n",
        "from pydub import AudioSegment\n",
        "from pyannote.audio import Pipeline\n",
        "import os\n",
        "\n",
        "\n",
        "video_url = \"https://www.youtube.com/watch?v=yX5EJf4R77s\"\n",
        "yt = YouTube(video_url)\n",
        "stream = yt.streams.filter(only_audio=True).first()\n",
        "audio_file_path = stream.download(filename=\"panel_discussion_audio.mp4\")\n",
        "\n",
        "audio = AudioSegment.from_file(audio_file_path, format=\"mp4\")\n",
        "audio_path = \"panel_discussion_audio.wav\"\n",
        "audio.export(audio_path, format=\"wav\")\n",
        "\n",
        "print(f\"Audio has been downloaded and converted to WAV format: {audio_path}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iYFMEtgAgORk",
        "outputId": "677f9608-ca91-4773-e1ea-d3a28404982c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Saved k/speaker_SPEAKER_03.wav\n",
            "Saved k/speaker_SPEAKER_01.wav\n",
            "Saved k/speaker_SPEAKER_00.wav\n",
            "Saved k/speaker_SPEAKER_02.wav\n"
          ]
        }
      ],
      "source": [
        "\n",
        "import os\n",
        "import torch\n",
        "import torchaudio\n",
        "import numpy as np\n",
        "from pydub import AudioSegment\n",
        "from pyannote.audio import Pipeline\n",
        "from transformers import AutoFeatureExtractor, AutoModelForAudioClassification, Wav2Vec2Processor\n",
        "\n",
        "HUGGING_FACE_TOKEN = os.getenv(\"HUGGING_FACE_KEY\")\n",
        "\n",
        "pipeline = Pipeline.from_pretrained(\n",
        "    \"pyannote/speaker-diarization-3.1\",\n",
        "    use_auth_token=HUGGING_FACE_TOKEN\n",
        ")\n",
        "\n",
        "audio_file = \"panel_discussion_audio.wav\"\n",
        "\n",
        "diarization = pipeline(audio_file)\n",
        "\n",
        "audio = AudioSegment.from_wav(audio_file)\n",
        "\n",
        "output_dir = \"k\"\n",
        "os.makedirs(output_dir, exist_ok=True)\n",
        "\n",
        "speaker_segments = {}\n",
        "\n",
        "for turn, _, speaker in diarization.itertracks(yield_label=True):\n",
        "    start_time = turn.start * 1000  # pydub works in milliseconds\n",
        "    end_time = turn.end * 1000\n",
        "    speaker_audio = audio[start_time:end_time]\n",
        "\n",
        "    if speaker not in speaker_segments:\n",
        "        speaker_segments[speaker] = [speaker_audio]\n",
        "    else:\n",
        "        speaker_segments[speaker].append(speaker_audio)\n",
        "\n",
        "audio_paths = []\n",
        "for speaker, segments in speaker_segments.items():\n",
        "    combined_audio = segments[0]\n",
        "    for segment in segments[1:]:\n",
        "        combined_audio += segment\n",
        "    output_file = os.path.join(output_dir, f\"speaker_{speaker}.wav\")\n",
        "    combined_audio.export(output_file, format=\"wav\")\n",
        "    audio_paths.append(output_file)\n",
        "    print(f\"Saved {output_file}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "99W2izUJVUAA",
        "outputId": "5059ec63-cc71-46e6-9a1f-d03e6077037d"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "Some weights of the model checkpoint at alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech were not used when initializing Wav2Vec2ForSequenceClassification: ['wav2vec2.encoder.pos_conv_embed.conv.weight_g', 'wav2vec2.encoder.pos_conv_embed.conv.weight_v']\n",
            "- This IS expected if you are initializing Wav2Vec2ForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).\n",
            "- This IS NOT expected if you are initializing Wav2Vec2ForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).\n",
            "Some weights of Wav2Vec2ForSequenceClassification were not initialized from the model checkpoint at alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech and are newly initialized: ['wav2vec2.encoder.pos_conv_embed.conv.parametrizations.weight.original0', 'wav2vec2.encoder.pos_conv_embed.conv.parametrizations.weight.original1']\n",
            "You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.\n",
            "100%|██████████| 3/3 [00:03<00:00,  1.31s/it]"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Number of male speakers: 3\n",
            "Number of female speakers: 1\n",
            "Total number of speakers: 4\n",
            "Gender identification completed for all speakers.\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "\n"
          ]
        }
      ],
      "source": [
        "import torchaudio\n",
        "from transformers import AutoFeatureExtractor, AutoModelForAudioClassification\n",
        "import tqdm\n",
        "from torch.utils.data import DataLoader\n",
        "\n",
        "\n",
        "class CustomDataset(torch.utils.data.Dataset):\n",
        "    def __init__(self, dataset, sampling_rate=16000, max_audio_len=5):\n",
        "        self.dataset = dataset\n",
        "        self.sampling_rate = sampling_rate\n",
        "        self.max_audio_len = max_audio_len\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.dataset)\n",
        "\n",
        "    def __getitem__(self, index):\n",
        "        filepath = self.dataset[index]\n",
        "        speech_array, sr = torchaudio.load(filepath)\n",
        "        if speech_array.shape[0] > 1:\n",
        "            speech_array = torch.mean(speech_array, dim=0, keepdim=True)\n",
        "        if sr != self.sampling_rate:\n",
        "            transform = torchaudio.transforms.Resample(sr, self.sampling_rate)\n",
        "            speech_array = transform(speech_array)\n",
        "        len_audio = speech_array.shape[1]\n",
        "        if len_audio < self.max_audio_len * self.sampling_rate:\n",
        "            padding = torch.zeros(1, self.max_audio_len * self.sampling_rate - len_audio)\n",
        "            speech_array = torch.cat([speech_array, padding], dim=1)\n",
        "        else:\n",
        "            speech_array = speech_array[:, :self.max_audio_len * self.sampling_rate]\n",
        "        speech_array = speech_array.squeeze().numpy()\n",
        "        return {\"input_values\": speech_array, \"attention_mask\": None}\n",
        "\n",
        "class CollateFunc:\n",
        "    def __init__(self, processor, padding=True, sampling_rate=16000):\n",
        "        self.processor = processor\n",
        "        self.padding = padding\n",
        "        self.sampling_rate = sampling_rate\n",
        "\n",
        "    def __call__(self, batch):\n",
        "        input_values = [item[\"input_values\"] for item in batch]\n",
        "        batch = self.processor(input_values, sampling_rate=self.sampling_rate, return_tensors=\"pt\", padding=self.padding)\n",
        "        return {\"input_values\": batch.input_values, \"attention_mask\": batch.attention_mask}\n",
        "\n",
        "def predict(test_dataloader, model, device):\n",
        "    model.to(device)\n",
        "    model.eval()\n",
        "    preds = []\n",
        "    with torch.no_grad():\n",
        "        for batch in tqdm.tqdm(test_dataloader):\n",
        "            input_values = batch['input_values'].to(device)\n",
        "            attention_mask = batch['attention_mask'].to(device)\n",
        "            logits = model(input_values, attention_mask=attention_mask).logits\n",
        "            scores = torch.nn.functional.softmax(logits, dim=-1)\n",
        "            pred = torch.argmax(scores, dim=1).cpu().detach().numpy()\n",
        "            preds.extend(pred)\n",
        "    return preds\n",
        "\n",
        "def get_gender(model_name_or_path, audio_paths, label2id, id2label, device):\n",
        "    num_labels = 2\n",
        "    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name_or_path)\n",
        "    model = AutoModelForAudioClassification.from_pretrained(\n",
        "        model_name_or_path, num_labels=num_labels, label2id=label2id, id2label=id2label\n",
        "    )\n",
        "    test_dataset = CustomDataset(audio_paths, max_audio_len=5)\n",
        "    data_collator = CollateFunc(processor=feature_extractor, padding=True, sampling_rate=16000)\n",
        "    test_dataloader = DataLoader(test_dataset, batch_size=16, collate_fn=data_collator, shuffle=False, num_workers=2)\n",
        "    preds = predict(test_dataloader=test_dataloader, model=model, device=device)\n",
        "    return preds\n",
        "\n",
        "model_name_or_path = \"alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech\"\n",
        "device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n",
        "label2id = {\"female\": 0, \"male\": 1}\n",
        "id2label = {0: \"female\", 1: \"male\"}\n",
        "\n",
        "audio_paths = []\n",
        "segments_dir = \"segments\"\n",
        "os.makedirs(segments_dir, exist_ok=True)\n",
        "\n",
        "speakers = {}\n",
        "speaker_id = 0\n",
        "\n",
        "for turn, _, speaker in diarization.itertracks(yield_label=True):\n",
        "    start_time = turn.start * 1000\n",
        "    end_time = turn.end * 1000\n",
        "    segment_audio = audio[start_time:end_time]\n",
        "\n",
        "    segment_path = os.path.join(segments_dir, f\"segment_{start_time}_{end_time}.wav\")\n",
        "    segment_audio.export(segment_path, format=\"wav\")\n",
        "    audio_paths.append(segment_path)\n",
        "\n",
        "    if speaker not in speakers:\n",
        "        speakers[speaker] = {\n",
        "            \"id\": speaker_id,\n",
        "            \"segments\": []\n",
        "        }\n",
        "        speaker_id += 1\n",
        "\n",
        "    speakers[speaker][\"segments\"].append(segment_path)\n",
        "\n",
        "preds = get_gender(model_name_or_path, audio_paths, label2id, id2label, device)\n",
        "\n",
        "for speaker in speakers:\n",
        "    speaker_gender_counts = {\"male\": 0, \"female\": 0}\n",
        "    for segment in speakers[speaker][\"segments\"]:\n",
        "        segment_index = audio_paths.index(segment)\n",
        "        predicted_gender = id2label[preds[segment_index]]\n",
        "        speaker_gender_counts[predicted_gender] += 1\n",
        "    speakers[speaker][\"gender\"] = max(speaker_gender_counts, key=speaker_gender_counts.get)\n",
        "\n",
        "male_count = 0\n",
        "female_count = 0\n",
        "\n",
        "for speaker in speakers:\n",
        "    gender = speakers[speaker][\"gender\"]\n",
        "    if gender == \"male\":\n",
        "        male_count += 1\n",
        "    elif gender == \"female\":\n",
        "        female_count += 1\n",
        "\n",
        "print(f\"Number of male speakers: {male_count}\")\n",
        "print(f\"Number of female speakers: {female_count}\")\n",
        "print(f\"Total number of speakers: {male_count + female_count}\")\n",
        "print(\"Gender identification completed for all speakers.\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "3c44mirEC9Q1"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_l3mLg3dlYE7"
      },
      "source": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "gpuType": "A100",
      "machine_shape": "hm",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
