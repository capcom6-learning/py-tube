# Metadata Service

Provides information about existed videos and register new videos.

## Configuration

Use enviroment variables to configure service:

* `PORT` - port to listen;
* `DBHOST` - MongoDB connection string without database name;
* `DBNAME` - name of database.

## Models

### Video

Video model represents single video.

* `_id` - unique video id;
* `name` - human readable name;
* `videoPath` - path to video in storage.

## Available routes

### GET /

Dummy route with service status.

### GET /video

Returns all registered videos.

### GET /video?id={id}

Return single video with given id or 404 if no such video exists.

### POST /video

Creates new video with given parameters. Accepts `application/json`.
