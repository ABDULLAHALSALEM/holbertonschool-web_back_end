#!/usr/bin/env python3
"""
Function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    
    Args:
        mongo_collection: pymongo collection object
        topic: topic searched
    
    Returns:
        List of schools that have the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
