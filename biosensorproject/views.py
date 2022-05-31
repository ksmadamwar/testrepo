import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.static import serve
from biosensorproject.settings import REACT_TEMPLATE_PATH


def index(request):
    # to serve react js view when loaded first
    return render(request, 'build/index.html')


def static_file_handler(request, folder, file):
    """Method to serve static files.
    The default static file middleware does not work in Azure Web App.
    Args:
        request: HttpRequest Object
        folder: Folder where the static file is stored (for e.g. media, js, css)
        file: Actual file name.
    Returns:
        The static file content.
    """
    if request.method == 'GET':
        static_file_path = os.path.join(
            REACT_TEMPLATE_PATH, "build", "static", folder, file)
        return serve(request, os.path.basename(static_file_path), os.path.dirname(static_file_path))