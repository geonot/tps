# Stage 1: Build the Vue.js application
FROM node:18-alpine AS build-stage
# Using -alpine for a smaller base image

WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies
# If you have a yarn.lock file, consider using yarn install --frozen-lockfile
RUN npm install

# Copy the rest of your application source code
COPY . .

# Environment variables for build stage (if any)
# Example: ARG VUE_APP_API_BASE_URL=/api
# Example: ENV VUE_APP_API_BASE_URL=$VUE_APP_API_BASE_URL

# Build the application
# This command might differ based on your project setup (e.g., if using TypeScript or specific build scripts)
RUN npm run build

# Stage 2: Serve the built application using Nginx
FROM nginx:stable-alpine

# Copy built assets from the build stage to Nginx's web root directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy the custom Nginx configuration file
# This replaces the default Nginx configuration.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 (default HTTP port Nginx listens on)
EXPOSE 80

# Command to run Nginx in the foreground
# This is standard practice for running Nginx in Docker.
CMD ["nginx", "-g", "daemon off;"]
