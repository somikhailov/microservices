FROM node:15-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ARG API=http://localhost:5000

RUN ROOT_API=${API} npm run build

EXPOSE 8080

CMD [ "node", "server.js" ]