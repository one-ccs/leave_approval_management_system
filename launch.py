#!/usr/bin/env python
# -*- coding: utf-8 -*-
from backend import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
