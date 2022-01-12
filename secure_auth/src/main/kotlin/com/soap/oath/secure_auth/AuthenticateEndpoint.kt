package com.soap.oath.secure_auth

import io.spring.guides.gs_producing_web_service.AuthenticateRequest
import io.spring.guides.gs_producing_web_service.AuthenticateResponse
import org.springframework.ws.server.endpoint.annotation.Endpoint
import org.springframework.ws.server.endpoint.annotation.PayloadRoot
import org.springframework.ws.server.endpoint.annotation.RequestPayload
import org.springframework.ws.server.endpoint.annotation.ResponsePayload

//@Endpoint
//class CountryEndpoint(val countryRepository: CountryRepository) {
//    companion object {
//        const val NAMESPACE_URI: String = "http://spring.io/guides/gs-producing-web-service"
//    }
//
//    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getCountryRequest")
//    @ResponsePayload
//    fun getCountry(@RequestPayload request: GetCountryRequest): GetCountryResponse? {
//        val response = GetCountryResponse()
//        response.country = countryRepository.findCountry(request.name)
//        return response
//    }
//}

@Endpoint
class AuthenticateEndpoint {
    companion object {
        const val NAMESPACE_URI: String = "http://spring.io/guides/gs-producing-web-service"
        val authValidator = AuthenticateJWTToken()
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "authenticateRequest")
    @ResponsePayload
    fun authenticate(@RequestPayload request: AuthenticateRequest): AuthenticateResponse? {
        val response = AuthenticateResponse()
        response.token = authValidator.checkTokenIntegrity(request.jwtdata)
        return response
    }
}