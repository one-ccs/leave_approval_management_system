#!/usr/bin/env python
# -*- coding: utf-8 -*-
from backend2 import flaskapp


if __name__ == '__main__':
    flaskapp.run(host='0.0.0.0', port=5001, debug=True)
