# Repository Information
Name: mikrotik-auction-app

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/animaacija/mikrotik-auction-app.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: Dockerfile
================================================
FROM mysql:5.7
COPY schema.sql /docker-entrypoint-initdb.d
================================================

File: apache.conf
================================================
<VirtualHost *:80>
    # The location of our projects public directory.
    DocumentRoot /var/www/html/public
    # Useful logs for debug.
    CustomLog /usr/logs/access.log common
    ErrorLog /usr/logs/error.log
    # Rewrites for pretty URLs, better not to rely on .htaccess.
    <Directory /var/www/html/public>
        <IfModule mod_rewrite.c>
            Options -MultiViews
            RewriteEngine On
            RewriteCond %{REQUEST_FILENAME} !-f
            RewriteRule ^ index.php [L]
        </IfModule>
    </Directory>
</VirtualHost>
================================================

File: Dockerfile
================================================
FROM php:7.2.9-apache-stretch
RUN docker-php-ext-install pdo_mysql
RUN a2enmod rewrite headers
COPY apache.conf /etc/apache2/conf-enabled/000-default.conf
COPY php.ini /usr/local/etc/php/php.ini
================================================

File: docker-compose.yml
================================================
version: "3"
services:
    db:
        restart: 'always'
        container_name: auction-mysql
        build:
            context: ./docker/mysql
        restart: always
        volumes:
            - $PWD/data-mysql:/var/lib/mysql
        environment:
            MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
            MYSQL_DATABASE: example
    composer:
      restart: 'no'
      container_name: composer
      image: composer
      command: composer install
      volumes:
        - $PWD/src/:/app
    php:
        restart: 'always'
        links:
            - db
        build:
            context: ./docker/phpApache
        container_name: auction-php
        ports:
            - 8080:80
        environment:
            APP_ENV: ${APP_ENV:-production}
        volumes:
            - $PWD/data-logs:/usr/logs
            - $PWD/src:/var/www/html
================================================

File: original-task-criteria.txt
================================================
[Uzdevums]
Jāizveido HTML un JS bāzēta lapa, kura sastāv no divām
loģiskām sadaļām.
1. ievades forma, kuru aizpildot var publicēt mantu izsolei.
2. saraksts ar izsolē pievienotajām mantām, tabulas veidā.
[1. daļas formas ievades lauki]
nosaukums - teksts 100 simboli, izgatavošanas gads - integer,
izvēlnes veidā pēdējie 15 gadi, sākumcena - decimālskaitlis,
parametri - apraksts zemāk
Parametrs sastāv no Nosaukuma un vērtības. Gan nosaukumu, gan vērtību
lietotājs var ievadīt pats. Lietotājs var dinamiski pievienot jaunu
parametru vai to dzēst.
Ievades formas apstiprināšanai jāattēlo poga. Nosūtot datus uz
serveri, tie jāsaglabā datubāzē un ielādējot lapu jāattēlo
2. daļas tabulā.
Formā visi lauki ir obligāti aizpildāmi un tas jāpārbauda ar
Javascript palīdzību pirms sūtīšanas.
[2. daļas saraksts]
Tiek attēlotas izsolē pievienotās mantas. Tabulas kolonnas:
1. pievienošanas datums un laiks,
2. nosaukums,
3. izgatavošanas gads,
4. sākumcena,
5. parametri - "parametra nosaukums": "vērtība". Katrs parametrs
jaunā rindā.
6. poga mantas dzēšanai - uzspiežot jāpārjautā. Dzēšana
jārealizē ar AJAX tehnoloģiju. Pēc dzēšanas jāpārlādē
tikai 2. daļas tabula.
[Atļautās tehnoloģijas:]
Publiskajai daļai: HTML, CSS, JavaScript (ieteicams jQuery)
Servera pusei:
Apache, Lighttpd vai Nginx serveris.
PHP 5+ (bez framework izmantošanas).
MySQL, PostgreSQL vai Firebird - datu saglabāšanai.
================================================

File: readme.md
================================================
# About
Lai projektu apskatītu pārlūkā:
 - `mkdir auction && cd $_`
 - `git clone https://gitlab.com/animaacija/mikrotik-auction-app.git .`
 - `docker-compose up`
 - iespējams, jāuzgaida kādas 5 minūtes, kamēr viss iesāk darboties
 - tad `open http://0.0.0.0:8080`
Realizēt uzdevuma punktus, jeb izpildot pašu minimumu, rezultātu var sasniegt ļoti ātri un samērā vienkārši.
Tāpēc, nolēmu gatavot šo mājasdarbu kā prezentāciju - kā iespēju man parādīt, ka, piemēram, `Trait` un `Interface` man nav svešums. Jauku lasīšanu!
Ir piedomāts, par gadījumu, ja klients ir atspējojis pārlūkā javascript, vai pat ja pārlūks nevalidē HTML5 formu - arī tad klientam tiks parādītas formas validācijas kļūdas. Pretējā gadījumā validācija un datu sūtīšana notiek caur javascript.
Konteksti:
 - Accessibility: web lapai jābūt "keyboard" interaktīvai.
 - Architecture: reizē ar šo aplikāciju ir tapis "Micro" frameworks `./src/app/`.
 - Logging: konceptuāli ieviesu `./data-logs/access.log`. 
 - 404: Atbilde par neatrastu lapu nāk no php, nevis servera konfigurācijas. 
 - Tests: eksistē testi, pagaidām tikai svarīgākie.
 - Api: uzturēt protokolu (konvenci) starp serveri un api metodēm, lai būtu vieglāks javascript.
 - Security: APP_ENV development.
 - Composer: tikai `twig` - tīrākam php.
 - Documentation: Konceptuāli tāda eksistē - skatīt zemāk.
------
# Development
Routes file: `./src/app/routes.php`
Configuration file: `./src/app/conf.php`
```bash
# to view exception messages, export APP_ENV=development
APP_ENV=development docker-compose up -d && docker logs composer -f
# run this to clear app cache
composer fresh
# runs tests
composer test
# run tests and view coverage
composer test-cover
# served at:
open http://0.0.0.0:8080
```
# Contribute
- We use PSR-2
- test all things
# Docker usage
```bash
# if initial project start,
# containers will take time to do `composer install`
# start infrastructure (production)
docker-compose up -d
# cli access database
docker exec -it auction-mysql mysql -uroot -Dexample
# reset all
docker system prune -a
```
================================================

File: composer.json
================================================
{
    "name": "animaacija/homework-mikrotik",
    "description": "Auction items CRUD app.",
    "type": "project",
    "license": "MIT",
    "autoload-dev": {
        "files": [
            "tests/bootstrap.php"
        ],
        "psr-4": {
            "": "tests/"
        }
    },
    "autoload": {
        "files": [
            "app/helpers.php",
            "app/routes.php"
        ],
        "psr-4": {
            "": "app/",
            "Auction\\": "Auction/"
        }
    },
    "authors": [
        {
            "name": "Martins Talbergs",
            "email": "animaacija@gmail.com"
        }
    ],
    "minimum-stability": "stable",
    "scripts": {
        "fresh": "rm -rf ./cache/*",
        "test": "vendor/bin/phpunit --colors=always",
        "test-cover": "vendor/bin/phpunit --colors=always --coverage-html=tests/coverage && open tests/coverage/index.html"
    },
    "require": {
        "php": "^7.2",
        "twig/twig": "^2.5"
    },
    "require-dev": {
        "phpunit/phpunit": "^7.3",
        "ivoba/dump-die-shortcuts": "^1.0"
    }
}
================================================

File: main.css
================================================
/* common */
body, html {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
    font-family: roboto, arial, sans-serif;
    color: #353535;
    background: #f5f5f5;
}
::-webkit-scrollbar {
    width: 2px;
}
::-webkit-scrollbar-thumb {
    background-color: #353535
}
h3, h1 {
    text-align: center;
}
table {
    border-spacing: 10px;
}
/* layout */
@supports (display: grid) {
    /* current grid support is ~80% */
    body {
        padding: 7px;
        display: grid;
        grid-template-rows: 70px auto 18px;
        grid-template-columns: auto auto;
        width: 100vw;
        height: 100vh;
        grid-column-gap: 4px;
    }
    body > footer {
        grid-column: 1 / -1;
        grid-row: 3 / span 1;
    }
    body > header {
        grid-column: 1 / -1;
        grid-row: 1 / span 1;
    }
    body > section {
        overflow-y: scroll;
    }
    body > section#table {
        grid-column: 1 / span 1;
        grid-row: 2 / span 1;
        word-break: break-all;
        white-space: pre-wrap;
    }
    body > section#form {
        grid-column: 2 / span 1;
        grid-row: 2 / span 1;
    }
}
@supports not (display: grid) {
    /* layout fallback */
    footer {
        position: fixed;
        bottom: 5px;
        left: 5px;
    }
    body > section {
        width: 50%;
        display: block;
        float: left;
    }
}
/* form & form-error */
.form-row > label::after {
    content: ':';
}
.form-row > label {
    margin: 5px;
}
.form-row {
    padding: 5px 10px;
    border-left: 5px #5e5e5e solid;
    display: block;
}
.error {
    color: red;
    padding: 0px 10px;
    font-size: 12px;
    font-family: monospace;
}
.error + .form-row::before {
    content: '*';
    font-size: 12px;
    color: red;
}
/* no-js & notice */
@keyframes slideInFromLeft {
    0% {transform: translateX(300%);}
    100% {transform: translateX(0);}
}
#no-js-msg {
    animation: 1s ease-out 0s 1 slideInFromLeft;
    padding: 30px;
    color: red;
    position: fixed;
    bottom: 0;
    right: 0;
}
.toast {
    position: fixed;
    bottom: 10px;
    font-size: 22px;
    padding: 20px;
    margin: 5px;
    border: 2px solid;
    display: inline-block;
}
/* botton */
button {
    position: relative;
    text-decoration: none;
    padding: 1px 7px 2px;
    font: 400 11px system-ui;
    transition: border, background-color .2s;
    border: #353535 solid 3px;
    background-color: #575757;
    margin: 0 10px;
    cursor: pointer;
    color: #f5f5f5;
}
button[disabled] {
    opacity: .4;
    cursor: not-allowed;
}
button:hover {
    border-color: #6a6a6a;
    background-color: #6a6a6a;
}
button:focus {
    background-color: #6a6a6a;
    outline-style: none;
    text-decoration: underline;
}
button.loading::before {
    content: 'loading..';
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    background: white;
    color: black;
    right: 0;
}
button.loading {
    pointer-events: none;
}
================================================

File: main.js
================================================
;/* <- good practice to start with semicolon.
*
* EcmaScript-5 safe code here.
* (+) sign and any other unary operator forces this function to be IIFE
* instance is exposed onto 'window' object namespace (only to illustrate easy development)
* */
+function(w, $) {
  /**
   * A simple protocol:
   * - server responds with array of errors in case of any type error
   * - server does not care about request method
   *
   * This factory just toggles "loading" states
   * and displays error messages.
   *
   * @param url
   * @param data
   * @param $loading
   * @param onSuccess
   * @param onError
   */
  function apiProtocol(url, data, $loading, onSuccess, onError) {
    onError = onError || function (msg) {
      App.message(msg);
    };
    function always() {
      $loading.removeClass('loading')
    }
    function done(resp) {
      if (typeof resp === 'string') {
        return fail()
      }
      if (resp.errors && resp.errors.length) {
        return resp.errors.forEach(onError);
      }
      onSuccess(resp)
    }
    function fail() {
      App.message('Network error.');
    }
    $loading.addClass('loading');
    $.post(url || '/', data || {}).always(always).done(done).fail(fail)
  }
  /**
   * Main object
   *
   * @param $table
   * @param $form
   * @param $messages
   * @constructor
   */
  function App($table, $form, $messages) {
    this.table = new AuctionTable($table);
    this.form = new AuctionForm($form);
    this.$messages = $messages
  }
  /**
   *
   * @param msg
   */
  App.prototype.message = function (msg) {
    var $node = $('<div/>', {text: msg, class: 'toast'});
    this.$messages.prepend($node);
    $node.on('click', function () {
      $node.remove()
    });
    setTimeout(function () {
      $node.click()
    }, 4000)
  };
  /**
   * Table object
   *
   * @param $table
   * @constructor
   */
  function AuctionTable($table) {
    this.ref = $table;
    this.$btnsDelete = $table.find('[data-action="delete"]', 'button');
    var that = this;
    this.$btnsDelete.on('click', function () {
      confirm('Are you sure?') && that.deleteItem($(this))
    });
  }
  /**
   *
   * @param $button
   */
  AuctionTable.prototype.deleteItem = function ($button) {
    function onSuccess () {
      $button.closest('[data-item-row]').remove()
    }
    apiProtocol(
      '/api/auction/items/delete',
      $button.data(),
      $button,
      onSuccess
    );
  };
  /**
   * Form object.
   * If javascript in browser is disabled - will do post.
   * Will validate before post
   *
   * @param $form
   * @constructor
   */
  function AuctionForm($form) {
    this.$form = $form;
    // caching few DOM queries
    this.$form.$inpTitle = this.$form.find('[name="title"]');
    this.$form.$inpYear = this.$form.find('[name="year_of_manufacture"]');
    this.$form.$inpPrice = this.$form.find('[name="initial_price"]');
    // Usually it's: `$form.on('submit', e => e.preventDefault() && validate())`
    // instead we "take over" button,
    // this way html validation will work if js is disabled
    this.$btnSubmit = $form.find('[type="submit"]', 'button');
    this.$btnSubmit.attr('type', 'button');
    this.$parametersContainer = $form.find('#parameters');
    this.parameters = [];
    this.$btnAddParameter = $form.find('#addParameter', 'button');
    this.$btnAddParameter.on('click', this.addParameter.bind(this));
    this.$btnSubmit.on('click', this.submit.bind(this));
    if (!this.$parametersContainer.length) {
      this.$btnAddParameter.attr('disabled', true);
      throw new Error("AuctionForm #parameters not found.")
    }
  }
  /**
   *
   */
  AuctionForm.prototype.removeErrors = function() {
    this.$form.find('.error').remove();
  };
  /**
   * sends out this form
   */
  AuctionForm.prototype.send = function() {
    this.removeErrors();
    apiProtocol(
      '/api/auction/items/store',
      this.$form.serializeArray(),
      this.$btnSubmit,
      function () {
        App.message("Success!");
        w.location.reload()
      },
      this.displayError.bind(this)
    );
  };
  /**
   * @param err
   */
  AuctionForm.prototype.displayError = function(err) {
    var errNode = w.document.createElement('div');
    errNode.classList.add('error');
    errNode.classList.add('form-row');
    errNode.textContent = err.reason;
    this.$form.find('[name="' + err.key + '"]')
      .closest('.form-row')
      .before(errNode)
  };
  /**
   * return array of found error objects
   */
  AuctionForm.prototype.validate = function() {
    var errors = [];
    ruleRequired.message = "Required.";
    function ruleRequired(val) {
      return !! val;
    }
    ruleLength.message = "Must not exceed 100 characters.";
    function ruleLength(val) {
      return val.length <= 100;
    }
    ruleGtZero.message = "Must me greater than zero.";
    function ruleGtZero(val) {
      return val > 0;
    }
    ruleFloating.message = "Two floating point precision limit.";
    function ruleFloating(val) {
      val = parseFloat(val);
      return parseFloat(val.toFixed(2)) >= val;
    }
    function runRules($inp, rules) {
      var val = $inp.val();
      while (cb = rules.shift()) {
        if (!cb(val)) {
          errors.push({
            key: $inp.attr('name'),
            reason: cb.message,
          });
          break;
        }
      }
    }
    function runParameterRules(param) {
      runRules(param.$node.$inpName, [ruleRequired, ruleLength]);
      runRules(param.$node.$inpValue, [ruleRequired, ruleLength]);
    }
    this.parameters.forEach(runParameterRules);
    runRules(this.$form.$inpTitle, [ruleRequired, ruleLength]);
    runRules(this.$form.$inpYear, [ruleRequired, ruleGtZero]);
    runRules(this.$form.$inpPrice, [ruleRequired, ruleGtZero, ruleFloating]);
    return errors;
  };
  /**
   *
   */
  AuctionForm.prototype.submit = function() {
    var errors = this.validate();
    if (errors.length) {
      this.removeErrors();
      errors.forEach(this.displayError.bind(this))
    } else {
      this.send();
    }
  };
  /**
   * adds next field
   */
  AuctionForm.prototype.addParameter = function() {
    var parameter = new AuctionFormParameter(this.parameters.length + 1);
    this.parameters.push(parameter);
    this.$parametersContainer.append(parameter.$node)
  };
  /**
   * ItemParameter object
   *
   * @param id
   * @constructor
   */
  function AuctionFormParameter(id) {
    this.$node = this.createNode(id)
  }
  /**
   * For sure, vanilla javascript would perform faster,
   * using jQuery only because so it's stated in task description.
   *
   * @param id
   * @returns {jQuery|HTMLElement}
   */
  AuctionFormParameter.prototype.createNode = function (id) {
    var $node = $('<div />', {class: 'form-row'});
    var nameId = 'parameterName' + id;
    var valueId = 'parameterValue' + id;
    var $name = $('<div />', {class: 'form-row'});
    var $value = $('<div />', {class: 'form-row'});
    $name.append($('<label />', {for: nameId, text: 'Name'}));
    $node.$inpName = $('<input />', {id: nameId, type: 'text', name: 'parameters[' + id + '][name]'});
    $name.append($node.$inpName);
    $value.append($('<label />', {for: valueId, text: 'Value'}));
    $node.$inpValue = $('<input />', {id: valueId, type: 'text', name: 'parameters[' + id + '][value]'});
    $value.append($node.$inpValue);
    $node.$removeBtn = $('<button />', {text: 'remove', class: 'btn-small'});
    $node.append([$name, $value]);
    $node.append($node.$removeBtn);
    $node.$removeBtn.on('click', this.remove.bind(this));
    return $node;
  };
  /**
   * Removes DOM node.
   * jQuery will automatically remove event handlers.
   */
  AuctionFormParameter.prototype.remove = function () {
    this.$node.prev('.error.form-row').remove();
    this.$node.remove();
  };
  /**
   * On DOM ready callback.
   */
  $(function () {
    $('#no-js-msg').remove();
    var app = new App(
      $('table'),
      $('form'),
      $('#messages')
    );
    App.message = app.message.bind(app);
    w.app = app
  })
}(window, jQuery);
================================================

File: 404.html
================================================
{% extends "main.html" %}
{% block content %}
<h1>Page not found.</h1>
{% endblock %}
================================================

File: auction_items_form.html
================================================
<form class="form-rows" method="post" action="/auction/items/store" id="newAuctionItem">
    {% include 'form_error.html' with {
        'err': oldInput.errorsKeyed.title
    } only %}
    <div class="form-row">
        <label for="item_title">Title</label>
        <input
                required maxlength="100"
                placeholder=""
                id="item_title"
                name="title"
                type="text"
                value="{{ oldInput.title }}"
        />
    </div>
    {% include 'form_error.html' with {
        'err': oldInput.errorsKeyed.year_of_manufacture
    } only %}
    <div class="form-row">
        <label for="year_of_manufacture">Year of manufacture</label>
        <select name="year_of_manufacture" id="year_of_manufacture">
            {% for year in years %}
                {% if oldInput.year_of_manufacture == year %}
                    <option selected="selected" value="{{ year }}">{{ year }}</option>
                {% else %}
                    <option value="{{ year }}">{{ year }}</option>
                {% endif %}
            {% endfor %}
        </select>
    </div>
    {% include 'form_error.html' with {
        'err': oldInput.errorsKeyed.initial_price}
    only %}
    <div class="form-row">
        <label for="initial_price">Initial price (EUR)</label>
        <input
                required min="0.01" step="0.01"
                placeholder="0,01"
                id="initial_price"
                name="initial_price"
                type="number"
                value="{{ oldInput.initial_price }}"
        />
    </div>
    <div class="form-row">
        <label>Parameters</label>
        <div id="parameters" class="form-rows"></div>
        <button id="addParameter" type="button">(+) Add parameter</button>
    </div>
    <button type="submit">Submit</button>
</form>
================================================

File: auction_items_home.html
================================================
{% extends "main.html" %}
{% block content %}
<section id="table">
    {{ include('auction_items_table.html') }}
</section>
<section id="form">
    {{ include('auction_items_form.html') }}
</section>
{% endblock %}
================================================

File: auction_items_table.html
================================================
<table>
    <thead>
        <th>Title</th>
        <th>Year of manufacture</th>
        <th>Initial price</th>
        <th>Parameters</th>
        <th>Created at</th>
        <th>Action</th>
    </thead>
    <tbody>
        {% for auctionItem in auctionItems %}
            <tr data-item-row>
                <td data-item-title>{{ auctionItem.title }}</td>
                <td>{{ auctionItem.yearOfManufacture }}</td>
                <td>&euro; {{ auctionItem.initialPriceEur }}</td>
                <td>
                    <ul>
                    {% for parameter in auctionItem.parameters %}
                        <li>{{ parameter.name }} - {{ parameter.value }}</li>
                    {% endfor %}
                    </ul>
                </td>
                <td>{{ auctionItem.createdAt }}</td>
                <td>
                    <button data-action="delete" data-id="{{ auctionItem.id }}">Delete</button>
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
================================================

File: form_error.html
================================================
{% if err %}
<div class="form-row error">
    {{ err.reason }}
</div>
{% endif %}
================================================

File: main.html
================================================
<html>
<head>
    <link rel="stylesheet" href="/css/main.css" />
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <title>Auction app</title>
</head>
<body>
    <header><h3>Auction item app at your service.</h3></header>
    {% block content %}{% endblock %}
    <footer>
        <div id="messages"></div>
        <div id="no-js-msg">Please consider enabling javascript.</div>
        {% block footer %}
            &copy; Copyright {{ "now"|date('Y') }}.
        {% endblock %}
    </footer>
    <script src="/js/jquery-3.3.1.min.js"></script>
    <script src="/js/main.js"></script>
</body>
</html>