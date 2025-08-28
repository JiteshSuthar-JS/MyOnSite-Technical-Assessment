.PHONY: build run stop test clean

build:
\tdocker build -t ai-db-designer-stub:latest .

run:
\tdocker compose up --build

stop:
\tdocker compose down

test:
\t@echo "Health check:"
\tcurl -s http://localhost:8000/health || true
\t@echo "\nUnified demo:"
\tcurl -s http://localhost:8000/demo/unified || true

clean:
\tdocker compose down -v || true
\tdocker rmi ai-db-designer-stub:latest || true
