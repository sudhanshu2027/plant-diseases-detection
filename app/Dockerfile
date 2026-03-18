# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Render uses dynamic PORT)
EXPOSE 8501

# Run Streamlit app
CMD streamlit run app/main.py --server.port=$PORT --server.address=0.0.0.0