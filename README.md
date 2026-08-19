# Borocito CMD

My personal implementation of my already implemented Borocito-Server and Borocito-CMD. All-in-One with Django.  

> And maybe the next gen Control System for Borocito instances.  

## Set-up

Borocito CTRL requiere: MySQL (opcional), Redis (requerido).

## TODO

### Borocito-CLI

   - send only response to a command, not complete structure
   - when starting, report information to update Instance model
   - tell borocito-cli to disable IDFTP. only allow if websocket config is enabled
      -  IDFTP=True
      -  WEBSOCKETS=True or boro-comm=True (boro-comm plugin handles websockets, and it a component, not embedded in CLI)

### Borocito-Extractor && Borocito-Updater

   - implement new infraestructure

### General

   - WAIT! : THERE ARE TWO WAYS TO SEND MESSAGES, ~IDFTP (borocito-cli default) for Borocito-CMD~ AND ~WEB-SOCKET (coming up for boro-comm)~
      - UI for IDFTP on CS (with htmx)
      - boro-comm websocket comms implementation
      - boro-comm starts with borocito (or windows) if regedit values says so
