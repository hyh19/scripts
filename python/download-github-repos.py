from urllib.request import urlretrieve
from urllib.parse import urlparse
import zipfile
import os

repo_url_list = []
with open("repos") as f:
    repo_url_list = f.read().splitlines()

for repo_url in repo_url_list:
    repo_info = urlparse(repo_url).path.split("/")
    user = repo_info[1]
    repo = repo_info[2]
    tag = repo_info[4]

    zip_file_url = "https://github.com/{user}/{repo}/archive/{tag}.zip".format(
        user=user, repo=repo, tag=tag)

    zip_file_name = "{user}-{repo}-{tag}.zip".format(user=user, repo=repo, tag=tag)

    # 下载压缩包
    urlretrieve(zip_file_url, zip_file_name)

    # 解压目录 
    unzip_dir = "{user}".format(user=user)

    # 解压压缩包
    with zipfile.ZipFile(zip_file_name) as f:
        f.extractall(path=unzip_dir)

    # 删除压缩包
    os.remove(zip_file_name)
