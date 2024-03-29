# bind-docker

This is an experiment to learn more about DNS, and to setup a trial environment.  Goals are:

1.  To setup a DNS server providing a private zone.
2.  Use the DNS server as a Public Key Infrastructure provider.
3.  Use the DNS server as a self-signed certificate distribution mechanism.

Full experiment is broken down into the steps below.

## Warning

This is for experimental use only!  It is not a suitable for production use.


## Step 1 - DNS lookup

- [x] Bind 9 in docker and accessible on port 5053
- [x] Create master zone `muppet.things`
- [x] Create zone `kermit.muppet.things`:
    - CDATA to `kermit.local`
- [x] Create zone `piggy.muppet.things`:
    - CDATA to `piggy.local`

### Tests
- [x] dig works - returns CDATA

    in `docker exec -it bind`:
    ```
    dig @localhost kermit.muppets.things
    ```

    in bash
    ```
    dig @localhost -p 5053 kermit.muppets.things
    ```


### Notes

- Restarting bind after editing zone files seems to be required.
- Odd error messages from bind
- CNAME records are being recursively looked up - need to look at behaviour when we have some services.


## Step 2 - PingPong

- [x] Setup `things` network
- [x] Setup resolver to use DNS
- [x] Setup `kermit` container - ping `piggy.muppet.things`
- [x] Setup `piggy` container - ping `kermit.muppet.things`

### Tests

- [x] `kermit` and `piggy` can ping each other on their `.things` network

### Notes

- Needed to change the forwarder settings in bind to use the docker forwarder
- Needed to disable dnssec (Hmmm - that feels wrong)


## Step 3.1 - Public keys in DNS

- [x] Basic webservice setup
- [x] Messages between services using `ns1`
- [ ] Add public keys to zone file
- [ ] Add private keys to `kermit` and `piggy` containers
- [ ] Fetch public keys using python and DNS lookup
- [ ] Encrypt message payload to destination
- [ ] Decrypt at destination

### Tests
- [x] Services work - can communicate with each other
- [ ] dig works - returns Pub KEY
- [ ] Encryption works


### Notes


## Step 3.2 - Certs in DNS, signed messages

- [ ] Add signing intermediate CA into `.muppet.things` zone
- [ ] Add certs signed by `muppet.things` IC to `piggy` and `kermit` zones
- [ ] Signed message from `piggy` - verify `kermit` can verify the message using cert in DNS.
- [ ] Encrypted reply to `piggy` - verify `kermit` can encrypt a message using cert and `piggy` can decrypt it using private key.

### Tests
- [ ] dig works - returns CERT
- [ ] Can verify certificate chain
- [ ] Signing works
- [ ] Encryption works

### Notes


## Step 4 - Revoking additional party

- [ ] Add `gonzo` container, with private key and cert in zone file to match configuration of `kermit` and `piggy`
- [ ] Verify `gonzo` can communicate with `kermit` and `piggy`
- [ ] Revoke `gonzo` certificate in DNS
- [ ] Verify `gonzo` signed requests are flagged as unverified by `piggy` and `kermit`
- [ ] Verify `piggy` and `kermit` cannot create a message for `gonzo` using `gonzo`'s cert

### Tests

- [ ] Revoked party cannot verify comms with remaining members
- [ ] Revoked party comms are flagged as unsigned and not trusted
