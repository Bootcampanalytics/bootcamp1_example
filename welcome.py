# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():

	products = ['active dry yeast','allspice','almond extract','almonds','apple juice','apples','applesauce','asparagus',
	'bacon','baking powder','baking soda','balsamic vinegar','bananas','basil','bay leaf','bay leaves','beef','black pepper',
	'boiling water','bread crumbs','bread flour','brown sugar','buttermilk','carrots','catsup','cayenne','cayenne pepper',
	'celery','cheddar cheese','chicken stock','chili powder','chopped nuts','chopped onion','chopped parsley','chopped pecans',
	'chopped walnuts','cider vinegar','cinnamon','cloves','cloves garlic','cold water','cornstarch','cream','cream cheese',
	'cumin','dijon mustard','dried apricots','dried oregano','dry mustard','dry white wine','egg whites','egg yolks',
	'extra virgin olive oil','fresh lemon juice','fresh parsley','garlic','garlic powder','garnish','ginger','granulated sugar',
	'grated parmesan cheese','green pepper','ground','ground beef','ground black pepper','ground cinnamon','ground cloves',
	'ground cumin','ground ginger','ground nutmeg','ground pepper','heavy cream','honey','juice','ketchup','lemon','lemon juice',
	'lime juice','margarine','melted butter','milk','minced garlic','molasses','mushrooms','note','nutmeg','oats','oil',
	'olive oil','onion','orange juice','oregano','packed brown sugar','paprika','parmesan cheese','parsley','pecans','pepper',
	'potatoes','powdered sugar','raisins','red onion','red wine vinegar','rice','ripe bananas','salt table','scallions',
	'shallots','skim milk','sour cream','soy sauce','stalks celery','stick','stick butter','strips','thyme','tomato paste',
	'tomato sauce','tomatoes','unsalted butter','vanilla','vanilla extract','vegetable','vegetable oil','vinegar','walnuts',
	'warm water','wheat flour','whipping cream','white pepper','worcestershire sauce','yeast']
	
	return render_template('index.htm', products=products)


	







port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
