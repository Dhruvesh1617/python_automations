#Write a Python script to build a Docker image from a Dockerfile and run a container from the image.
import os
import docker
import docker.errors

def build_docker_image(dockerfile_path,image_name):
    client=docker.from_env() # this helps to fetch docker methods 
    print(f"printing docker image from {dockerfile_path}")
    try:
        image,logs=client.images.build(path=dockerfile_path,tag=image_name,rm=True)
        #method for building image
        
        #to fetch logs
        for log in logs:
            if 'stream' in log:
                print(log['stream'].strip()) #strip used to remove whitespace
        print(f"Image {image_name} built successfully")
        print (f"image details:{image}")
        return image
    
    except docker.errors.BuildError as e:
        print(f"Error building image:{e}")
        return None
    
def run_docker_container(image_name):
    client = docker.from_env()

    # Run the container
    print(f"Running container from image {image_name}...")
    try:
        container = client.containers.run(image_name, detach=True, tty=True)
        print(f"Container {container.id} is running...")
        return container
    except docker.errors.APIError as e:
        print(f"Error during container run: {e}")
        return None

def main():
    dockerfile_path=os.path.abspath(".")#mention path  of dockerfile
    image_name="custom_img:latest"
    image=build_docker_image(dockerfile_path,image_name)
    if image:
       container=run_docker_container(image_name)
       if container:
            print(f"Container {container.id} is running in the background.")
    




if __name__=='__main__':
    main()
