# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:55:51 2021

@author: ANUSHKA
"""
#Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

#Building a Blockchain
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1, prev_hash='0')
        
    def create_block(self, proof, prev_hash):
        block={'index': len(self.chain)+1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'prev_hash': prev_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        prev_block=self.chain[-1]
        return prev_block
    
#Mining our Blockchain