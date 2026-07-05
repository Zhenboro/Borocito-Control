# Borocito CMD

My personal implementation of my already implemented Borocito-Server and Borocito-CMD. All-in-One with Django.  

> And maybe the next gen Control System for Borocito instances.  

## TODO

### Borocito-CS

   - ~~when instance send telemetry log, write it to an file inside telemetry/~~

### Borocito-CLI

   - ~~check configuration api~~
   - ~~when starting, report information to update Instance model~~
   - ~~send telemetry to endpoint in order to create a .log file~~
   - tell borocito-cli to disable IDFTP. only allow if websocket config is enabled
      -  IDFTP=True
      -  WEBSOCKETS=True or boro-comm=True (boro-comm plugin handles websockets, and it a component, not embedded in CLI)

### ~~Borocito-Updater~~

   - ~~implement new infraestructure~~

### boro-get

   - boro-get check components api
   - boro-get download with components api config
   - use .net webclient class for downloads, as github downloads may not work with My.Network

### General

   - REVIEW KEY-PAIR LOGIC : las key-pairs son las llaves requeridas para hacer peticiones al servidor. actualmente, es una key-pair por instancia. (SEGUIR POR AHORA)
      - REVIEW : y si la key-pair son para obtener un slot instancia con una llave que es devuelta para que la instancia comienze a usar esa???? (PARA EL FUTURO: usar id de instancia)

   - TODO : Adapt Borocito-CLI software to work with Borocito-CS by default. ??????? (la retrocompatibilidad se perdera)

   - WAIT! : THERE ARE TWO WAYS TO SEND MESSAGES, ~IDFTP (borocito-cli default) for Borocito-CMD~ AND ~WEB-SOCKET (coming up for boro-comm)~
      - UI for IDFTP on CS (with htmx)
      - ~~boro-comm websocket comms implementation~~
      - boro-comm starts with borocito (or windows) if regedit values says so

   - SHIT: es mejor usar websockets a IDFTP, pero el miedo es que algo falle.
