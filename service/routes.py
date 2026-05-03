"""
Routes for the CI/CD Final Project Flask application
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Root endpoint"""
    return jsonify(
        status=200,
        message="CI/CD Final Project is running!"
    )


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify(
        status="OK"
    )
