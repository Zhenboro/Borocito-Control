# Borocito CMD

My personal implementation of my already implemented Borocito-Server and Borocito-CMD. All-in-One with Django.  

> And maybe the next gen Control System for Borocito instances.  

## Set-up

Borocito CTRL requiere: MySQL (opcional), Redis (requerido).

## TODO

i f*cking lost EVERYTHING. NOW, ALL OVER AGAIN.

### Borocito-CLI

   - check configuration api
   - when starting, report information to update Instance model
   - send telemetry to endpoint in order to create a .log file
   - tell borocito-cli to disable IDFTP. only allow if websocket config is enabled
      -  IDFTP=True
      -  WEBSOCKETS=True or boro-comm=True (boro-comm plugin handles websockets, and it a component, not embedded in CLI)

### Borocito-Updater

   - implement new infraestructure

### boro-get

   - boro-get check components api
   - boro-get download with components api config
   - use .net webclient class for downloads, as github downloads may not work with My.Network

### General

   - TODO : Usar KeyPair inicialmente para crear un Reporte de Infectado. Al crearse la instancia en el servidor, usar el ID devuelto como llave para enviar peticiones. KeyPair debe ser ELIMINADA COMPLETAMENTE despues de esta primera interacion.
      BASICAMENTE:
         - KeyPar es para crear una instancia y preparar el servidor.
         - La ID devuelta es para la comunicacion Servidor-Cliente, nada mas.

   - TODO : Adapt Borocito-CLI software to work with Borocito-CS by default. ??????? (la retrocompatibilidad se perdera)

   - WAIT! : THERE ARE TWO WAYS TO SEND MESSAGES, ~IDFTP (borocito-cli default) for Borocito-CMD~ AND ~WEB-SOCKET (coming up for boro-comm)~
      - UI for IDFTP on CS (with htmx)
      - boro-comm websocket comms implementation
      - boro-comm starts with borocito (or windows) if regedit values says so

   - SHIT: es mejor usar websockets a IDFTP, pero el miedo es que algo falle.
