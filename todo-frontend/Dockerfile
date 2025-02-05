# Use official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy project files
COPY . .

# Build React app
RUN npm run build

# Install Serve (static file server)
RUN npm install -g serve

# Expose port for React
EXPOSE 3000

# Start frontend app
CMD ["serve", "-s", "build", "-l", "3000"]
