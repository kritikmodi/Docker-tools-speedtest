import subprocess
import time

def tag_docker_image_using_crane(image_path, new_tag):
    try:
        command = ["crane", "tag", image_path, new_tag]
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    except subprocess.CalledProcessError as e:
        print(f"Error tagging image {image_path} with {new_tag}: {e}")

def tag_docker_image_using_imagetools(image_path, new_tag):
    try:
        command = [
            'docker', 'buildx', 'imagetools', 'create',
            image_path, '--tag', new_tag
        ]
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    except subprocess.CalledProcessError as e:
        print(f"Error tagging image {image_path} with {new_tag}: {e}")

def tag_docker_image_using_docker(image_path, image_path_with_new_tag):
    try:
        subprocess.run(['docker', 'pull', image_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['docker', 'tag', image_path, image_path_with_new_tag], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['docker', 'push', image_path_with_new_tag], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
    except subprocess.CalledProcessError as e:
        print(f"Error tagging image {image_path} with {new_tag}: {e}")

counter = 1

image_path = input("Enter image path without any tag : ")

old_tag = input("Input any old tag to grab the manifest from : ")

new_tag = f"testing{counter}"

image_path_with_old_tag = f"{image_path}:{old_tag}"

image_path_with_new_tag = f"{image_path}:{new_tag}"

start = time.time()
tag_docker_image_using_crane(image_path_with_old_tag, new_tag)
end = time.time()

print("Crane execution time :", (end-start) * 10**3, "ms")

counter=counter+1

new_tag = f"testing{counter}"
image_path_with_new_tag = f"{image_path}:{new_tag}"

start = time.time()
tag_docker_image_using_imagetools(image_path_with_old_tag, image_path_with_new_tag)
end = time.time()

print("Imagetools execution time :", (end-start) * 10**3, "ms")

counter=counter+1

new_tag = f"testing{counter}"
image_path_with_new_tag = f"{image_path}:{new_tag}"

start = time.time()
tag_docker_image_using_docker(image_path_with_old_tag, image_path_with_new_tag)
end = time.time()

print("Docker execution time :", (end-start) * 10**3, "ms")
