package com.momen.mochat

import java.net.ServerSocket

class Server {

    companion object {
        private var server: ServerSocket? = null

        fun instance(): ServerSocket {
            if (server == null)
                server = ServerSocket(9999)
            return server!!
        }
    }


}