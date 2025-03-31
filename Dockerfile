FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libnss3 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libxss1 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Install Playwright
RUN pip install playwright

# Install Playwright browsers
RUN playwright install --with-deps

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Copy the source code into the container
COPY . .

# Add the current directory to PYTHONPATH
ENV PYTHONPATH=/app

# Set display to use virtual framebuffer if needed
ENV DISPLAY=:99

# Set the command to run the agent
CMD ["poetry", "run", "python", "src/agent/main.py"]