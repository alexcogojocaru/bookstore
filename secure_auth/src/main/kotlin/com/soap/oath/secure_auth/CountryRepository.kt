package com.soap.oath.secure_auth

import io.spring.guides.gs_producing_web_service.Country
import io.spring.guides.gs_producing_web_service.Currency
import org.springframework.stereotype.Component
import org.springframework.util.Assert
import javax.annotation.PostConstruct

@Component
class CountryRepository {
    companion object {
        val countries: HashMap<String, Country> = hashMapOf()
    }

    @PostConstruct
    fun initData() {
        val spain = Country()
        spain.name = "Spain"
        spain.capital = "Madrid"
        spain.currency = Currency.EUR
        spain.population = 46704314

        val poland = Country()
        poland.name = "Poland"
        poland.capital = "Warsaw"
        poland.currency = Currency.PLN
        poland.population = 38186860

        val uk = Country()
        uk.name = "United Kingdom"
        uk.capital = "London"
        uk.currency = Currency.GBP
        uk.population = 63705000

        countries[spain.name] = spain
        countries[poland.name] = poland
        countries[uk.name] = uk
    }

    fun findCountry(name: String): Country? {
        Assert.notNull(name, "The country's name must not be null")
        return countries[name]
    }
}