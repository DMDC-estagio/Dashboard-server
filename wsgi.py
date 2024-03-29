from app import app, routes


app.register_blueprint(routes.indexRouter)
app.register_blueprint(routes.logsRouter)
app.register_blueprint(routes.groupRouter)
app.register_blueprint(routes.chartRouter)

app.register_blueprint(routes.logsApiRouter, url_prefix='/api')

if __name__ == "__main__":
    app.run(threaded=True, debug=True)