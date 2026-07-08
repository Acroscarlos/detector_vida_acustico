conda create --name usar_gpu_env python=3.10 pip -y
conda activate usar_gpu_env
pip install tensorflow==2.10.0 librosa==0.10.1 soundfile==0.12.1 numpy==1.23.5 scikit-learn matplotlib jupyter --no-cache-dir
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0 -y


import tensorflow as tf
print("Versión de TF:", tf.version)
print("¿GPU Disponible?:", tf.config.list_physical_devices('GPU'))


pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install setuptools==69.5.1