build:
	cd frontend; npm run build
	docker-compose build

run: build
	docker-compose-run