import sublime, sublime_plugin
import sys 
import os

sys.path.append(os.path.dirname(__file__))

import websocket

class LivePreview(sublime_plugin.EventListener):
  def __init__(self, *args, **kwargs):
    """Initialize a new instance."""
    super().__init__(*args, **kwargs)
    self.ws = websocket.create_connection("ws://localhost:8099/socket")

  def on_activated(self, view):
    name = view.file_name()
    if name is not None:
      self.ws.send(name)

  # def on_deactivated(self, view):
  #   name = view.file_name()
  #   if name is not None:
  #     self.ws.send("deactivate:" + name)
