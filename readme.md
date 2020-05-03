**Set up project locally**

1. Install Python 3.8.2  https://www.python.org/downloads/windows/
2. Install Django `py -m pip install Django` in cmd
3. Install Docker   https://hub.docker.com/editions/community/docker-ce-desktop-windows/
4. `git clone https://gl.knu.ua/friedsoup/kazkaprod.git`
-------------------------------------------------------------------------------

**Start working with project**

1. Open project folder, where Dockerfile is located.
2. `docker-compose up --build`
3. Work.

-------------------------------------------------------------------------------

**Useful commands**

1. Clear docker system and images
    
`docker system prune -f`

`docker image prune -af`

2. Stop docker container

`docker-compose down`

3. Show docker containers

`docker ps`

4. Enter docker container

For Windows: `winpty docker exec -it <container ID> bash`

For Linux: `docker exec -it <container ID> bash`
