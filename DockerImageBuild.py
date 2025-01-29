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
    


def main():
    dockerfile_path=os.path.abspath(".")
    image_name="custom_img:latest"
    build_docker_image(dockerfile_path,image_name)
    




if __name__=='__main__':
    main()
