package com.soap.oath.secure_auth

import io.jsonwebtoken.Jwts
import io.jsonwebtoken.SignatureAlgorithm
import io.spring.guides.gs_producing_web_service.AuthRequest
import io.spring.guides.gs_producing_web_service.AuthResponse
import io.spring.guides.gs_producing_web_service.ValidateRequest
import io.spring.guides.gs_producing_web_service.ValidateResponse
import org.springframework.ws.server.endpoint.annotation.Endpoint
import org.springframework.ws.server.endpoint.annotation.PayloadRoot
import org.springframework.ws.server.endpoint.annotation.RequestPayload
import org.springframework.ws.server.endpoint.annotation.ResponsePayload
import java.lang.Exception
import java.util.*

@Endpoint
class OauthEndpoint {
    companion object {
        const val NAMESPACE_URI: String = "http://spring.io/guides/gs-producing-web-service"
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "authRequest")
    @ResponsePayload
    fun getJWTToken(@RequestPayload authRequest: AuthRequest): AuthResponse {
        val response = AuthResponse()

        response.token = Jwts.builder()
            .setSubject(authRequest.sub)
            .setExpiration(Date(2023, 1, 1))
            .setIssuer(authRequest.iss)
            .signWith(SignatureAlgorithm.HS512, "MTIzNDU2Nzg=").compact()
        return response
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "validateRequest")
    @ResponsePayload
    fun validateToken(@RequestPayload validateRequest: ValidateRequest): ValidateResponse {
        val response = ValidateResponse()

        try {
            response.response = Jwts.parser().setSigningKey("MTIzNDU2Nzg=").parseClaimsJws(validateRequest.token).body.toString()
        } catch (e: Exception) {
            response.response = "Invalid JWT Token"
        }
        return response
    }
}