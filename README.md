<p align="center">
  <a href="https://github.com/yilbegan/telefuck">
    <img src="https://raw.githubusercontent.com/yilbegan/telefuck/master/images/logo_light.png" style="image-rendering: pixelated; image-rendering: crisp-edges;" alt="Telefuck">
  </a>
</p>
<h1 align="center">
    Telegram bot written in brainfuck and python
</h1>
<p align="center">
  <img alt="Code Quality" src="https://img.shields.io/codacy/grade/4eb122242c294386a61dc26c143e91a9?style=flat-square">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/yilbegan/telefuck?style=flat-square">
  <img alt="Code Style" src="https://img.shields.io/badge/code%20style-black-black?style=flat-square">
</p>

## Installation

```
$ pip install -r requirements.txt
$ export TELEGRAM_TOKEN=<...>
$ python -m app
```

## Docker

```
$ docker pull ghcr.io/yilbegan/telefuck:latest
$ docker run -e TELEGRAM_TOKEN=<...> ghcr.io/yilbegan/telefuck:latest
```

## Commands

Command | Description
:-----: | :-----------------:
`/h`    | Show help message
`/g`    | Play small RPG
`/s`    | Show high score

## Todo

- [ ] Add more games
- [ ] Optimize interpeter
