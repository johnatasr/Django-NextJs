
FROM node:alpine AS runner
WORKDIR /app

RUN apk add --no-cache libc6-compat

COPY package.json ./
RUN npm install

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

COPY --chown=nextjs:nodejs . .

USER nextjs

EXPOSE 3000

CMD ["npm", "run", "dev"]

