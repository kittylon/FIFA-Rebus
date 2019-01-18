from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/FifaDB"
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return render_template('base.html', title='Fifa World Cup')


@app.route('/registrar_equipo', methods=['GET', 'POST'])
def register_team():
    """
    Creates a fifa team within the DB.
    :return: GET METHOD: renders the template and the context variable country_names (list of all countries for the
    fifa teams)
    POST METHOD: Message if the team was created or if an error occurred; plus the response code.
    """
    if request.method == 'POST':
        result = request.form.to_dict()
        data = mongo.db.teams.insert_one(result)
        if data:
            return "team created successfully", 200
        return "An error occurred, please try again", 400
    countries = list(mongo.db.countries.find())
    country_names = sorted([country['name'] for country in countries])
    return render_template('new_team.html', countries=country_names)


@app.route('/registrar_jugador', methods=['GET', 'POST'])
def register_player():
    """
    Creates a player team within the DB.
    :return: GET METHOD: renders the template and the context variable teams (list of all teams already created
    in the DB)
    POST METHOD: Message if the player was created or if an error occurred; plus the response code.
    """
    if request.method == 'POST':
        result = request.form.to_dict()
        data = mongo.db.players.insert_one(result)
        if data:
            return "player created successfully", 200
        return "An error occurred, please try again", 400
    teams = list(mongo.db.teams.find())
    teams_name = sorted([team['team_name'] for team in teams])
    return render_template('new_player.html', teams=teams_name)


@app.route('/registrar_tecnico', methods=['GET', 'POST'])
def register_coach():
    """
    Creates a team coach within the DB.
    :return: GET METHOD: renders the template and the context variable teams (list of all teams already created
    in the DB)
    POST METHOD: Message if the coach was created or if an error occurred; plus the response code.
    """
    if request.method == 'POST':
        result = request.form.to_dict()
        data = mongo.db.coaches.insert_one(result)
        if data:
            return "Coach created successfully", 200
        return "An error occurred, please try again", 400
    teams = list(mongo.db.teams.find())
    teams_name = sorted([team['team_name'] for team in teams])
    countries = list(mongo.db.countries.find())
    country_names = sorted([country['name'] for country in countries])
    return render_template('new_coach.html', teams=teams_name, nationalities=country_names)


@app.route('/reporte', methods=['GET', 'POST'])
def create_report():
    teams_count = count_teams()
    titular_players = count_players()
    youngest_player = get_youngest_player()
    oldest_player = get_oldest_player()
    report = {"teams_count": teams_count,
              "titular_players": titular_players,
              "youngest_player": youngest_player,
              "oldest_player": oldest_player}
    return jsonify(report)


def count_teams():
    teams_count = mongo.db.teams.count()
    return teams_count


def count_players():
    players_count = mongo.db.players.find({"is_titular": True})
    players_count = players_count.count()
    return players_count


def get_youngest_player():
    youngest_player = dict(mongo.db.players.find_one(sort=[("birth_date", 1)]))
    del youngest_player['_id']
    return youngest_player


def get_oldest_player():
    oldest_player = dict(mongo.db.players.find_one(sort=[("birth_date", -1)]))
    del oldest_player['_id']
    return oldest_player


def avg_bench_players():
    # teams_count = mongo.db.teams.count()
    # avg_bench_players  = mongo.db.players.find({"is_titular": False})
    # del oldest_player['_id']
    return True


if __name__ == '__main__':
    app.run()
