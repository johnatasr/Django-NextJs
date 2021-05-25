
FROM node:alpine AS runner
WORKDIR /app

RUN apk add --no-cache libc6-compat

COPY package.json ./
RUN npm install

COPY . /app

EXPOSE 3000

CMD ["npm", "run", "dev"]

