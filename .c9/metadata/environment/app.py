{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":["i"],"id":115},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"insert","lines":["c"]}],[{"start":{"row":26,"column":33},"end":{"row":26,"column":34},"action":"insert","lines":["e"],"id":116},{"start":{"row":26,"column":34},"end":{"row":26,"column":35},"action":"insert","lines":["s"]},{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"insert","lines":["1"]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"remove","lines":["x"],"id":117},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["d"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["n"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["c"],"id":118},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["h"]}],[{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["o"],"id":119},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["c"],"id":120},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["e"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"remove","lines":["x"],"id":121},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["e"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["d"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"remove","lines":["n"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["i"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["c"],"id":122},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["h"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["o"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["i"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["c"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":19},"action":"remove","lines":["choic1"],"id":123},{"start":{"row":24,"column":13},"end":{"row":24,"column":21},"action":"insert","lines":["choices1"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":15},"action":"remove","lines":["@app.route('/')"],"id":124}],[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""],"id":125}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":126}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":15},"action":"insert","lines":["@app.route('/')"],"id":127}],[{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":128}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":34},"action":"insert","lines":["from bson.objectid import ObjectId"],"id":129}],[{"start":{"row":43,"column":40},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":130},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":4},"end":{"row":50,"column":53},"action":"insert","lines":["@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)"],"id":131}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "],"id":132}],[{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"remove","lines":["s"],"id":133},{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"remove","lines":["k"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"remove","lines":["s"]},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"remove","lines":["a"]},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"insert","lines":["b"],"id":134},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"insert","lines":["o"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"insert","lines":["k"],"id":135}],[{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"remove","lines":["k"],"id":136},{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"remove","lines":["s"]},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"remove","lines":["a"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"remove","lines":["t"]}],[{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["b"],"id":137},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"insert","lines":["o"]},{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"insert","lines":["o"]}],[{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"insert","lines":["k"],"id":138}],[{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"remove","lines":["s"],"id":139},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"remove","lines":["a"]},{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"remove","lines":["t"]}],[{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"insert","lines":["b"],"id":140},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"insert","lines":["o"],"id":141},{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"insert","lines":["k"]}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"remove","lines":["k"],"id":142},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"remove","lines":["s"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"remove","lines":["a"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["b"],"id":143},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["o"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["k"],"id":144}],[{"start":{"row":49,"column":47},"end":{"row":49,"column":48},"action":"remove","lines":["k"],"id":145},{"start":{"row":49,"column":46},"end":{"row":49,"column":47},"action":"remove","lines":["s"]},{"start":{"row":49,"column":45},"end":{"row":49,"column":46},"action":"remove","lines":["a"]},{"start":{"row":49,"column":44},"end":{"row":49,"column":45},"action":"remove","lines":["t"]}],[{"start":{"row":49,"column":44},"end":{"row":49,"column":45},"action":"insert","lines":["b"],"id":146},{"start":{"row":49,"column":45},"end":{"row":49,"column":46},"action":"insert","lines":["o"]}],[{"start":{"row":49,"column":46},"end":{"row":49,"column":47},"action":"insert","lines":["o"],"id":147},{"start":{"row":49,"column":47},"end":{"row":49,"column":48},"action":"insert","lines":["k"]}],[{"start":{"row":49,"column":56},"end":{"row":49,"column":57},"action":"remove","lines":["k"],"id":148},{"start":{"row":49,"column":55},"end":{"row":49,"column":56},"action":"remove","lines":["s"]},{"start":{"row":49,"column":54},"end":{"row":49,"column":55},"action":"remove","lines":["a"]},{"start":{"row":49,"column":53},"end":{"row":49,"column":54},"action":"remove","lines":["t"]}],[{"start":{"row":49,"column":53},"end":{"row":49,"column":54},"action":"insert","lines":["b"],"id":149},{"start":{"row":49,"column":54},"end":{"row":49,"column":55},"action":"insert","lines":["o"]},{"start":{"row":49,"column":55},"end":{"row":49,"column":56},"action":"insert","lines":["o"]}],[{"start":{"row":49,"column":56},"end":{"row":49,"column":57},"action":"insert","lines":["k"],"id":150}],[{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"remove","lines":["k"],"id":151}],[{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"remove","lines":["k"],"id":152},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"remove","lines":["s"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"remove","lines":["a"]},{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"remove","lines":["t"]}],[{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"insert","lines":["v"],"id":153},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"insert","lines":["b"]},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"insert","lines":["o"],"id":154}],[{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"remove","lines":["o"],"id":155},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"remove","lines":["o"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"remove","lines":["b"]},{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"remove","lines":["v"]}],[{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"insert","lines":["b"],"id":156},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"insert","lines":["o"]},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"insert","lines":["k"],"id":157}],[{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"remove","lines":["k"],"id":158},{"start":{"row":45,"column":26},"end":{"row":45,"column":27},"action":"remove","lines":["s"]},{"start":{"row":45,"column":25},"end":{"row":45,"column":26},"action":"remove","lines":["a"]},{"start":{"row":45,"column":24},"end":{"row":45,"column":25},"action":"remove","lines":["t"]}],[{"start":{"row":45,"column":24},"end":{"row":45,"column":25},"action":"insert","lines":["b"],"id":159},{"start":{"row":45,"column":25},"end":{"row":45,"column":26},"action":"insert","lines":["o"]}],[{"start":{"row":45,"column":26},"end":{"row":45,"column":27},"action":"insert","lines":["o"],"id":160},{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"insert","lines":["k"]}],[{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"remove","lines":["k"],"id":161},{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"remove","lines":["s"]},{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"remove","lines":["a"]},{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"remove","lines":["t"]}],[{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"insert","lines":["b"],"id":162},{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"insert","lines":["o"]},{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"insert","lines":["k"],"id":163}],[{"start":{"row":47,"column":59},"end":{"row":47,"column":60},"action":"remove","lines":["k"],"id":164},{"start":{"row":47,"column":58},"end":{"row":47,"column":59},"action":"remove","lines":["s"]},{"start":{"row":47,"column":57},"end":{"row":47,"column":58},"action":"remove","lines":["a"]},{"start":{"row":47,"column":56},"end":{"row":47,"column":57},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":56},"end":{"row":47,"column":57},"action":"insert","lines":["b"],"id":165},{"start":{"row":47,"column":57},"end":{"row":47,"column":58},"action":"insert","lines":["o"]},{"start":{"row":47,"column":58},"end":{"row":47,"column":59},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":59},"end":{"row":47,"column":60},"action":"insert","lines":["k"],"id":166}],[{"start":{"row":50,"column":53},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":167},{"start":{"row":51,"column":0},"end":{"row":51,"column":27},"action":"insert","lines":["                           "]},{"start":{"row":51,"column":27},"end":{"row":52,"column":0},"action":"insert","lines":["",""]},{"start":{"row":52,"column":0},"end":{"row":52,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":52,"column":0},"end":{"row":52,"column":1},"action":"insert","lines":["v"],"id":168}],[{"start":{"row":52,"column":0},"end":{"row":52,"column":1},"action":"remove","lines":["v"],"id":169},{"start":{"row":51,"column":27},"end":{"row":52,"column":27},"action":"remove","lines":["","                           "]}],[{"start":{"row":51,"column":27},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":170},{"start":{"row":52,"column":0},"end":{"row":52,"column":27},"action":"insert","lines":["                           "]}],[{"start":{"row":52,"column":0},"end":{"row":63,"column":41},"action":"insert","lines":["@app.route('/update_task/<task_id>', methods=[\"POST\"])","def update_task(task_id):","    tasks = mongo.db.tasks","    tasks.update( {'_id': ObjectId(task_id)},","    {","        'task_name':request.form.get('task_name'),","        'category_name':request.form.get('category_name'),","        'task_description': request.form.get('task_description'),","        'due_date': request.form.get('due_date'),","        'is_urgent':request.form.get('is_urgent')","    })","    return redirect(url_for('get_tasks'))"],"id":171}],[{"start":{"row":52,"column":23},"end":{"row":52,"column":24},"action":"remove","lines":["k"],"id":172},{"start":{"row":52,"column":22},"end":{"row":52,"column":23},"action":"remove","lines":["s"]},{"start":{"row":52,"column":21},"end":{"row":52,"column":22},"action":"remove","lines":["a"]},{"start":{"row":52,"column":20},"end":{"row":52,"column":21},"action":"remove","lines":["t"]}],[{"start":{"row":52,"column":20},"end":{"row":52,"column":21},"action":"insert","lines":["b"],"id":173},{"start":{"row":52,"column":21},"end":{"row":52,"column":22},"action":"insert","lines":["o"]},{"start":{"row":52,"column":22},"end":{"row":52,"column":23},"action":"insert","lines":["o"]}],[{"start":{"row":52,"column":23},"end":{"row":52,"column":24},"action":"insert","lines":["k"],"id":174}],[{"start":{"row":52,"column":29},"end":{"row":52,"column":30},"action":"remove","lines":["k"],"id":175},{"start":{"row":52,"column":28},"end":{"row":52,"column":29},"action":"remove","lines":["s"]},{"start":{"row":52,"column":27},"end":{"row":52,"column":28},"action":"remove","lines":["a"]},{"start":{"row":52,"column":26},"end":{"row":52,"column":27},"action":"remove","lines":["t"]}],[{"start":{"row":52,"column":26},"end":{"row":52,"column":27},"action":"insert","lines":["b"],"id":176},{"start":{"row":52,"column":27},"end":{"row":52,"column":28},"action":"insert","lines":["o"]},{"start":{"row":52,"column":28},"end":{"row":52,"column":29},"action":"insert","lines":["o"]}],[{"start":{"row":52,"column":29},"end":{"row":52,"column":30},"action":"insert","lines":["k"],"id":177}],[{"start":{"row":53,"column":14},"end":{"row":53,"column":15},"action":"remove","lines":["k"],"id":178},{"start":{"row":53,"column":13},"end":{"row":53,"column":14},"action":"remove","lines":["s"]},{"start":{"row":53,"column":12},"end":{"row":53,"column":13},"action":"remove","lines":["a"]},{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"remove","lines":["t"]}],[{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"insert","lines":["b"],"id":179},{"start":{"row":53,"column":12},"end":{"row":53,"column":13},"action":"insert","lines":["o"]},{"start":{"row":53,"column":13},"end":{"row":53,"column":14},"action":"insert","lines":["o"]},{"start":{"row":53,"column":14},"end":{"row":53,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":53,"column":14},"end":{"row":53,"column":15},"action":"remove","lines":["o"],"id":180}],[{"start":{"row":53,"column":14},"end":{"row":53,"column":15},"action":"insert","lines":["k"],"id":181}],[{"start":{"row":53,"column":18},"end":{"row":53,"column":19},"action":"remove","lines":["s"],"id":182},{"start":{"row":53,"column":17},"end":{"row":53,"column":18},"action":"remove","lines":["a"]}],[{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"remove","lines":["t"],"id":183}],[{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"insert","lines":["b"],"id":184},{"start":{"row":53,"column":17},"end":{"row":53,"column":18},"action":"insert","lines":["o"]},{"start":{"row":53,"column":18},"end":{"row":53,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"remove","lines":["s"],"id":185},{"start":{"row":55,"column":36},"end":{"row":55,"column":37},"action":"remove","lines":["a"]},{"start":{"row":55,"column":35},"end":{"row":55,"column":36},"action":"remove","lines":["t"]}],[{"start":{"row":55,"column":35},"end":{"row":55,"column":36},"action":"insert","lines":["b"],"id":186},{"start":{"row":55,"column":36},"end":{"row":55,"column":37},"action":"insert","lines":["o"]},{"start":{"row":55,"column":37},"end":{"row":55,"column":38},"action":"insert","lines":["o"]}],[{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"remove","lines":["e"],"id":187},{"start":{"row":60,"column":15},"end":{"row":60,"column":16},"action":"remove","lines":["t"]},{"start":{"row":60,"column":14},"end":{"row":60,"column":15},"action":"remove","lines":["a"]},{"start":{"row":60,"column":13},"end":{"row":60,"column":14},"action":"remove","lines":["d"]},{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"remove","lines":["_"]}],[{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"insert","lines":["="],"id":188},{"start":{"row":60,"column":13},"end":{"row":60,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":60,"column":13},"end":{"row":60,"column":14},"action":"remove","lines":["="],"id":189},{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"remove","lines":["="]},{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"remove","lines":["e"]},{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"remove","lines":["u"]},{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"remove","lines":["d"]}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["s"],"id":190},{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"insert","lines":["t"]},{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"insert","lines":["a"]}],[{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"insert","lines":["r"],"id":191}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":13},"action":"remove","lines":["star"],"id":192},{"start":{"row":60,"column":9},"end":{"row":60,"column":20},"action":"insert","lines":["star_rating"]}],[{"start":{"row":60,"column":48},"end":{"row":60,"column":49},"action":"remove","lines":["e"],"id":193},{"start":{"row":60,"column":47},"end":{"row":60,"column":48},"action":"remove","lines":["t"]},{"start":{"row":60,"column":46},"end":{"row":60,"column":47},"action":"remove","lines":["a"]},{"start":{"row":60,"column":45},"end":{"row":60,"column":46},"action":"remove","lines":["d"]},{"start":{"row":60,"column":44},"end":{"row":60,"column":45},"action":"remove","lines":["_"]},{"start":{"row":60,"column":43},"end":{"row":60,"column":44},"action":"remove","lines":["e"]}],[{"start":{"row":60,"column":42},"end":{"row":60,"column":43},"action":"remove","lines":["u"],"id":194},{"start":{"row":60,"column":41},"end":{"row":60,"column":42},"action":"remove","lines":["d"]}],[{"start":{"row":60,"column":41},"end":{"row":60,"column":42},"action":"insert","lines":["s"],"id":195},{"start":{"row":60,"column":42},"end":{"row":60,"column":43},"action":"insert","lines":["t"]},{"start":{"row":60,"column":43},"end":{"row":60,"column":44},"action":"insert","lines":["a"]}],[{"start":{"row":60,"column":44},"end":{"row":60,"column":45},"action":"insert","lines":["r"],"id":196}],[{"start":{"row":60,"column":41},"end":{"row":60,"column":45},"action":"remove","lines":["star"],"id":197},{"start":{"row":60,"column":41},"end":{"row":60,"column":52},"action":"insert","lines":["star_rating"]}],[{"start":{"row":63,"column":37},"end":{"row":63,"column":38},"action":"remove","lines":["s"],"id":198},{"start":{"row":63,"column":36},"end":{"row":63,"column":37},"action":"remove","lines":["k"]},{"start":{"row":63,"column":35},"end":{"row":63,"column":36},"action":"remove","lines":["s"]},{"start":{"row":63,"column":34},"end":{"row":63,"column":35},"action":"remove","lines":["a"]},{"start":{"row":63,"column":33},"end":{"row":63,"column":34},"action":"remove","lines":["t"]}],[{"start":{"row":63,"column":33},"end":{"row":63,"column":34},"action":"insert","lines":["b"],"id":199},{"start":{"row":63,"column":34},"end":{"row":63,"column":35},"action":"insert","lines":["o"]},{"start":{"row":63,"column":35},"end":{"row":63,"column":36},"action":"insert","lines":["o"]},{"start":{"row":63,"column":36},"end":{"row":63,"column":37},"action":"insert","lines":["k"]}],[{"start":{"row":63,"column":40},"end":{"row":63,"column":67},"action":"remove","lines":["                           "],"id":200},{"start":{"row":63,"column":40},"end":{"row":64,"column":0},"action":"insert","lines":["",""]},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":4},"end":{"row":65,"column":0},"action":"insert","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":65,"column":4},"end":{"row":69,"column":0},"action":"insert","lines":["@app.route('/delete_task/<task_id>')","def delete_task(task_id):","    mongo.db.tasks.remove({'_id': ObjectId(task_id)})","    return redirect(url_for('get_tasks'))",""],"id":201}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":202}],[{"start":{"row":65,"column":22},"end":{"row":65,"column":23},"action":"remove","lines":["s"],"id":203},{"start":{"row":65,"column":21},"end":{"row":65,"column":22},"action":"remove","lines":["a"]},{"start":{"row":65,"column":20},"end":{"row":65,"column":21},"action":"remove","lines":["t"]}],[{"start":{"row":65,"column":20},"end":{"row":65,"column":21},"action":"insert","lines":["b"],"id":204},{"start":{"row":65,"column":21},"end":{"row":65,"column":22},"action":"insert","lines":["o"]},{"start":{"row":65,"column":22},"end":{"row":65,"column":23},"action":"insert","lines":["o"]}],[{"start":{"row":65,"column":28},"end":{"row":65,"column":29},"action":"remove","lines":["s"],"id":205},{"start":{"row":65,"column":27},"end":{"row":65,"column":28},"action":"remove","lines":["a"]},{"start":{"row":65,"column":26},"end":{"row":65,"column":27},"action":"remove","lines":["t"]}],[{"start":{"row":65,"column":26},"end":{"row":65,"column":27},"action":"insert","lines":["b"],"id":206},{"start":{"row":65,"column":27},"end":{"row":65,"column":28},"action":"insert","lines":["o"]},{"start":{"row":65,"column":28},"end":{"row":65,"column":29},"action":"insert","lines":["o"]}],[{"start":{"row":66,"column":19},"end":{"row":66,"column":20},"action":"remove","lines":["k"],"id":207},{"start":{"row":66,"column":18},"end":{"row":66,"column":19},"action":"remove","lines":["s"]},{"start":{"row":66,"column":17},"end":{"row":66,"column":18},"action":"remove","lines":["a"]},{"start":{"row":66,"column":16},"end":{"row":66,"column":17},"action":"remove","lines":["t"]}],[{"start":{"row":66,"column":16},"end":{"row":66,"column":17},"action":"insert","lines":["b"],"id":208},{"start":{"row":66,"column":17},"end":{"row":66,"column":18},"action":"insert","lines":["o"]},{"start":{"row":66,"column":18},"end":{"row":66,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":66,"column":19},"end":{"row":66,"column":20},"action":"insert","lines":["k"],"id":209}],[{"start":{"row":67,"column":45},"end":{"row":67,"column":46},"action":"remove","lines":["s"],"id":210},{"start":{"row":67,"column":44},"end":{"row":67,"column":45},"action":"remove","lines":["a"]},{"start":{"row":67,"column":43},"end":{"row":67,"column":44},"action":"remove","lines":["t"]}],[{"start":{"row":67,"column":43},"end":{"row":67,"column":44},"action":"insert","lines":["b"],"id":211},{"start":{"row":67,"column":44},"end":{"row":67,"column":45},"action":"insert","lines":["o"]},{"start":{"row":67,"column":45},"end":{"row":67,"column":46},"action":"insert","lines":["o"]}],[{"start":{"row":68,"column":37},"end":{"row":68,"column":38},"action":"remove","lines":["s"],"id":212},{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"remove","lines":["k"]},{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"remove","lines":["s"]},{"start":{"row":68,"column":34},"end":{"row":68,"column":35},"action":"remove","lines":["a"]},{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"remove","lines":["t"]}],[{"start":{"row":68,"column":33},"end":{"row":68,"column":34},"action":"insert","lines":["b"],"id":213},{"start":{"row":68,"column":34},"end":{"row":68,"column":35},"action":"insert","lines":["o"]},{"start":{"row":68,"column":35},"end":{"row":68,"column":36},"action":"insert","lines":["o"]}],[{"start":{"row":68,"column":36},"end":{"row":68,"column":37},"action":"insert","lines":["k"],"id":214}],[{"start":{"row":69,"column":0},"end":{"row":70,"column":0},"action":"remove","lines":["",""],"id":215},{"start":{"row":68,"column":40},"end":{"row":69,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":472.875,"scrollleft":0,"selection":{"start":{"row":68,"column":40},"end":{"row":68,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":46,"state":"start","mode":"ace/mode/python"}},"timestamp":1583335348002,"hash":"d519a5f5a35272e3d7cf4b9585bf264af0499f2a"}