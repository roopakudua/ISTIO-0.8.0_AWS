# Istio

[![CircleCI](https://circleci.com/gh/istio/istio.svg?style=shield)](https://circleci.com/gh/istio/istio)
[![Go Report Card](https://goreportcard.com/badge/github.com/istio/istio)](https://goreportcard.com/report/github.com/istio/istio)
[![GoDoc](https://godoc.org/github.com/istio/istio?status.svg)](https://godoc.org/github.com/istio/istio)
[![codecov.io](https://codecov.io/github/istio/istio/coverage.svg?branch=master)](https://codecov.io/github/istio/istio?branch=master)

An open platform to connect, manage, and secure microservices.

- [Introduction](#introduction)
- [Repositories](#repositories)
- [Issue management](#issue-management)

In addition, here are some other documents you may wish to read:

- [Istio Community](https://github.com/istio/community) - describes how to get involved and contribute to the Istio project
- [Istio Developer's Guide](https://github.com/istio/istio/wiki/Dev-Guide) - explains how to set up and use an Istio development environment
- [Project Conventions](https://github.com/istio/istio/wiki/Dev-Conventions) - describes the conventions we use within the code base
- [Creating Fast and Lean Code](https://github.com/istio/istio/wiki/Dev-Writing-Fast-and-Lean-Code) - performance-oriented advice and guidelines for the code base

You'll find many other useful documents on our [Wiki](https://github.com/istio/istio/wiki).

## Introduction

Istio is an open platform for providing a uniform way to integrate
microservices, manage traffic flow across microservices, enforce policies
and aggregate telemetry data. Istio's control plane provides an abstraction
layer over the underlying cluster management platform, such as Kubernetes,
Mesos, etc.

Visit [istio.io](https://istio.io) for in-depth information about using Istio.

Istio is composed of these components:

- **Envoy** - Sidecar proxies per microservice to handle ingress/egress traffic
   between services in the cluster and from a service to external
   services. The proxies form a _secure microservice mesh_ providing a rich
   set of functions like discovery, rich layer-7 routing, circuit breakers,
   policy enforcement and telemetry recording/reporting
   functions.

  > Note: The service mesh is not an overlay network. It
  > simplifies and enhances how microservices in an application talk to each
  > other over the network provided by the underlying platform.

- **Mixer** - Central component that is leveraged by the proxies and microservices
   to enforce policies such as authorization, rate limits, quotas, authentication, request
   tracing and telemetry collection.

- **Pilot** - A component responsible for configuring the proxies at runtime.

- **Citadel** - A centralized component responsible for certificate issuance and rotation.

- **Node Agent** - A per-node component responsible for certificate issuance and rotation.

- **Broker** - A component implementing the [Open Service Broker API](https://github.com/openservicebrokerapi/servicebroker) for Istio-based services. (Under development)

Istio currently supports Kubernetes, Consul, and Eureka-based environments. We plan support for additional platforms such as
Cloud Foundry, and Mesos in the near future.

## Repositories

The Istio project is divided across a few GitHub repositories.

- [istio/istio](README.md). This is the main repository that you are
currently looking at. It hosts Istio's core components and also
the sample programs and the various documents that govern the Istio open source
project. It includes:
  - [security](security/). This directory contains security related code,
including Citadel (acting as Certificate Authority), node agent, etc.
  - [pilot](pilot/). This directory
contains platform-specific code to populate the
[abstract service model](https://istio.io/docs/concepts/traffic-management/overview.html), dynamically reconfigure the proxies
when the application topology changes, as well as translate
[routing rules](https://istio.io/docs/reference/config/traffic-rules/routing-rules.html) into proxy specific configuration.
  - [istioctl](istioctl/). This directory contains code for the
[_istioctl_](https://istio.io/docs/reference/commands/istioctl.html) command line utility.
  - [mixer](mixer/). This directory
contains code to enforce various policies for traffic passing through the
proxies, and collect telemetry data from proxies and services. There
are plugins for interfacing with various cloud platforms, policy
management services, and monitoring services.
  - [broker](broker/). This directory
contains code for Istio's implementation of the Open Service Broker API.

- [istio/api](https://github.com/istio/api). This repository defines
component-level APIs and common configuration formats for the Istio platform.

- [istio/mixerclient](https://github.com/istio/mixerclient). Client libraries
(currently supports C++) for Mixer's API.

- [istio/proxy](https://github.com/istio/proxy). The Istio proxy contains
extensions to the [Envoy proxy](https://github.com/envoyproxy/envoy) (in the form of
Envoy filters), that allow the proxy to delegate policy enforcement
decisions to Mixer.

## Issue management

We use GitHub combined with ZenHub to track all of our bugs and feature requests. Each issue we track has a variety of metadata:

- **Epic**. An epic represents a feature area for Istio as a whole. Epics are fairly broad in scope and are basically product-level things.
Each issue is ultimately part of an epic.

- **Milestone**. Each issue is assigned a milestone. This is 0.1, 0.2, ..., or 'Nebulous Future'. The milestone indicates when we
think the issue should get addressed.

- **Priority/Pipeline**. Each issue has a priority which is represented by the Pipeline field within GitHub. Priority can be one of
P0, P1, P2, or >P2. The priority indicates how important it is to address the issue within the milestone. P0 says that the
milestone cannot be considered achieved if the issue isn't resolved.

We don't annotate issues with Releases; Milestones are used instead. We don't use GitHub projects at all, that
support is disabled for our organization.
## ISTIO-0.8.0_AWS
How this configured istio is different from the other [istio](https://istio.io/)?

- **Background**. 
The Istio that we get from here is not customised to work with kubernetes cluster running on AWS.It was difficult to access the user exposable services like(Prometheus,Servicegraph,Grafana Dashboard).

- **What we have done?**.
If you open [this](https://github.com/avkumar19/ISTIO-0.8.0_AWS/tree/master/install/kubernetes) you will find lot of YAML files related to Istio set up and our customisation for aws is currently available for these two setups:-

   1. istio-demo.yaml (open [this](https://github.com/avkumar19/ISTIO-0.8.0_AWS/commit/d1b4f4c6fd7bb8c8339047ad93c119c28ef48591#diff-ea7fbc5ced6fe779070ff1df273a7af2) to view changes)

   2. istio-demo-auth.yaml (open [this](https://github.com/avkumar19/ISTIO-0.8.0_AWS/commit/d1b4f4c6fd7bb8c8339047ad93c119c28ef48591#diff-ea7fbc5ced6fe779070ff1df273a7af2) to view changes).

- **Reason for Doing So?**.
Since we were not able to access user exposible services, So we created LoadBalancers based on the requirnment of those services. And after that we were able to access the services using their corresponding Loadbalancer's IP along with appropriate port no.

- **ISTIO-0.8.0_AWS in Action**.
For setting up the AWS configured istio we need clone this repository and apply YAML files using the same commands present in istio [documentaion](https://istio.io/docs/setup/kubernetes/quick-start/).After doing so you are all set to explore the amazing features of Istio. 
