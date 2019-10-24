# Copyright (c) 2015 Pixomondo
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the MIT License included in this
# distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the MIT License. All rights
# not expressly granted therein are reserved by Pixomondo.

"""
Geometry Output App for Houdini
"""

import sgtk


class GeometryOutputNode(sgtk.platform.Application):
    def init_app(self):
        module = self.import_module("tk_houdini_geometrynode")
        self.handler = module.ToolkitGeometryNodeHandler(self)

    def convert_to_geometry_nodes(self):
        """
        Convert all Shotgun Geometry nodes found in the current Script to regular
        Geometry nodes. Additional toolkit information will be stored in
        user data named 'tk_*'
        """
        self.handler.convert_sg_to_geometry_nodes()

    def convert_from_geometry_nodes(self):
        """
        Convert all regular Geometry nodes that have previously been converted
        from Shotgun Geometry nodes, back into Shotgun Geometry nodes.
        """
        self.handler.convert_geometry_to_sg_nodes()
    
    def get_work_file_template(self):
        """
        Returns the configured work file template for the app.
        """

        return self.get_template("work_file_template")

    def get_output_path(self, node):
        """
        Returns the evaluated output path for the supplied node.
        """

        self.log_debug("Retrieving output path for %s" % (node,))

        output_path = self.handler.get_output_path(node)
        self.log_debug("Retrieved output path: %s" % (output_path,))
        return output_path