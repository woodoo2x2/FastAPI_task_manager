docker_test_up:
	sudo docker compose -f docker-compose.test.yml up -d

docker_test_down:
	sudo docker compose -f docker-compose.test.yml down

docker_up:
	sudo docker compose -f docker-compose.dev.yml up --build -d

docker_down:
	sudo docker compose -f docker-compose.dev.yml down